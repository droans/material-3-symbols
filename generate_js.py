#!/usr/bin/env python3
import logging as log
import json
from glob import glob
import os
from os.path import (
    basename,
    splitext,
    join as path_join,
)
from shutil import (
    copytree,
    move as move_file
)
from string import Template
import subprocess
from xml.dom.minidom import Document, parse
from git import Repo
class Const:
    SVG = "svg"
    DEFAULT_LOG_LEVEL = log.INFO
    OUTPUT_PATH = 'dist/material-symbols.js'
    VALIDATE_DIR = 'validate'
    OUTPUT_PATH_SYMBOLS_JSON = f'{VALIDATE_DIR}/symbols.json'
    CHANGELOG_OUTPUT_PATH = f'{VALIDATE_DIR}/changelog.md'
    CHANGELOG_SVG_DIR = f'{VALIDATE_DIR}/svg'

log.basicConfig(level=Const.DEFAULT_LOG_LEVEL)

def get_path(dom: Document) -> str:
    """Get the path of the svg file."""
    return dom.getElementsByTagName("path")[0].getAttribute("d")


def get_keywords(dom: Document) -> str:
    """Get the keywords of the svg file."""
    desc_tags = dom.getElementsByTagName("desc")
    if len(desc_tags) > 0 and desc_tags[0].firstChild is not None:
        return desc_tags[0].firstChild.nodeValue.split(" ")
    else:
        return []

def create_icon_maps(icon_base_path):
    dirs = os.listdir(icon_base_path)
    log.info(f'Checking {dirs}')
    log.debug(f'CWD: {os.getcwd()}')
    result = {}
    for d in dirs:
        log.debug(f'Checking in {path_join(icon_base_path, d, f"*.{Const.SVG}")}')
        doms = [
            (basename(splitext(file)[0]), parse(file)) for file in glob(path_join(icon_base_path, d, f"*.{Const.SVG}"))
        ]
        log.debug(f'Doms: {doms}')
        for file_name, dom in doms:
            tmp = {
                'path': get_path(dom),
                "keywords": get_keywords(dom)
            }
            icon_name = f'{file_name}-{d}'
            result[icon_name] = tmp
    return result

def save_symbols_json(symbols: dict):
    with open(Const.OUTPUT_PATH_SYMBOLS_JSON, 'w') as f:
        f.write(json.dumps(symbols))
    return

def open_symbols_json() -> dict:
    if not os.path.exists(Const.OUTPUT_PATH_SYMBOLS_JSON):
        return {}
    with open(Const.OUTPUT_PATH_SYMBOLS_JSON, 'r') as f:
        return json.loads(f.read())

def make_svg_html(svg_path, symbol_name):
    svg = f'''
<svg width="42px" height="42px" xmlns="http://www.w3.org/2000/svg">
    <path d="{svg_path}"></path>
</svg>'''
    file_path = f'{Const.CHANGELOG_SVG_DIR}/{symbol_name}.svg'
    save_path = f'./{Const.CHANGELOG_SVG_DIR}/{symbol_name}.svg'
    save_symbols_svg(svg, save_path)
    return f'![{symbol_name}]({file_path})'

def save_symbols_svg(svg_html, svg_path):
    with open(svg_path, 'w') as f:
        f.write(svg_html)

def compare_old_new_symbols(new_symbols: dict):
    old_symbols = open_symbols_json()
    added = []
    removed = []
    changed = []
    for k, v in new_symbols.items():
        if k not in old_symbols:
            added.append(k)
        else:
            new_path = v.get('path')
            old_path = old_symbols[k]['path']
            if new_path != old_path:
                new_svg = make_svg_html(new_path, f'new-{k}')
                old_svg = make_svg_html(old_path, f'old-{k}')
                tmp = f'{k} (New: {new_svg}, Old: {old_svg})'
                changed.append(tmp)
    
    for k in old_symbols.keys():
        if k not in new_symbols:
            removed.append(k)
    result = {}
    if len(added):
        result['added'] = added
    if len(removed):
        result['removed'] = removed
    if len(changed):
        result['changed'] = changed
    return result

def create_symbol_changelog(new_symbols: dict):
    changed_symbols = compare_old_new_symbols(new_symbols)
    base_changelog = '# Symbol Changelog:'
    if changed_symbols == {}:
        base_changelog += '\nNo changes'
    else:
        for k, v in changed_symbols.items():
            log.info(f'Handling changes {k}')
            base_changelog += '\n'
            base_changelog += (f'##{k}:\n  *')
            base_changelog += '\n  * '.join(v)
    with open(Const.CHANGELOG_OUTPUT_PATH, 'w') as f:
        f.write(base_changelog)
    save_symbols_json(new_symbols)
    return
    
def generate_icon_js(icon_path):
    icon_map = create_icon_maps(icon_path)
    create_symbol_changelog(icon_map)
    template = Template(
        """const MS_ICONS_MAP = $ICONS;

async function getIcon(name) {
    return {path: MS_ICONS_MAP[name]?.path};
    }
async function getIconList() {
    return Object.entries(MS_ICONS_MAP).map(([icon, content]) => ({
        name: icon,
        keywords: content.keywords,
    }));
}

window.customIcons = window.customIcons || {};
window.customIcons["m3s"] = { getIcon, getIconList };

window.customIconsets = window.customIconsets || {};
window.customIconsets["m3s"] = getIcon;
"""
    )

    js = template.substitute(ICONS=json.dumps(icon_map, sort_keys=True, indent=2))
    return js

def save_js(js, output_path=Const.OUTPUT_PATH):
    with open(output_path, 'w') as f:
        f.write(js)

def check_repo_for_changes(repo_path):
    """ Run git fetch --dry-run and check if up-to-date """
    cur_dir = os.getcwd()
    os.chdir(repo_path)
    
    # Use try-except just to ensure path changes back...
    try:
        cmd = ['git', 'fetch', '--dry-run']
        output = subprocess.run(cmd, capture_output=True, text=True)
    
        # Seems to output to stderr - checking both to be safe...
        if output.stdout == '':
            proc_result = output.stderr
        os.chdir(cur_dir)
        return proc_result != ''
    except e as Exception:
        os.chdir(cur_dir)
        raise e

def pull_symbols_from_repo(repo_path):
    log.info(f'Pulling repo at {repo_path}')
    repo = Repo(repo_path)
    log.debug(f'Repo Working Dir: {repo.working_dir}')
    repo.remotes.origin.pull()
    log.debug(f'Successfully pulled repo')

def move_symbols(base_src_dir, base_dest_dir):
    log.info(f'Moving symbols from {base_src_dir} to {base_dest_dir}')
    src_dirs = listdir(base_src_dir)
    log.debug(f'Source dirs: {','.join(src_dirs)}')
    for d in src_dirs:
        src_dir = path_join(base_src_dir, d)
        dest_dir = path_join(base_dest_dir, d)
        log.info(f'Copying {src_dir} to {dest_dir}')
        copytree(src_dir, dest_dir, dirs_exist_ok=True)

def update_symbols():
    log.info('Updating symbols...')
    repo_path = path_join('raw/material-symbols')
    if not check_repo_for_changes(repo_path):
        log.info(f'No changes detected, not pulling or moving symbols')
        return
    pull_symbols_from_repo(repo_path)
    src_dir = path_join(repo_path, 'custom_components/material_symbols/data')
    dest_dir = 'svg'
    move_symbols(src_dir, dest_dir)


def main():
    update_symbols()
    js = generate_icon_js('svg')
    save_js(js)

if __name__ == '__main__':
    main()