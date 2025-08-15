base_repo_dir=raw
base_files_dir="/custom_components/material_symbols/data"
repo_path="material-symbols"
validate_dir=validate
validate_svg_dir=${validate_dir}/svg
repo="https://github.com/beecho01/${repo_path}"

make_dir_if_not_exist() {
  if ! test -d ${@}; then
    echo "${@} folder does not exist, creating now..."
    echo ""
    mkdir ${@};
  else
    echo "${@} folder already exists, not recreating.";
  fi
}
make_dir_if_not_exist ${base_repo_dir}
make_dir_if_not_exist ${validate_dir}
make_dir_if_not_exist ${validate_svg_dir}

cd ${base_repo_dir}
if test -d ${repo_path}; then
  echo "Repo already exists, not continuing."
  exit;
fi

echo "Cloning Repo with depth=1, filter=tree:0"
echo ""
git clone -n --depth=1 --filter=tree:0 ${repo}
cd ${repo_path}
echo ""
echo "Performing sparse checkout"
git sparse-checkout set --no-cone ${base_files_dir}/m3o ${base_files_dir}/m3of ${base_files_dir}/m3r ${base_files_dir}/m3rf ${base_files_dir}/m3s ${base_files_dir}/m3sf
echo ""
echo "Performing checkout..."
echo ""
git checkout