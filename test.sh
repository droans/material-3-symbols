base_repo_dir=raw2
base_files_dir="/custom_components/material_symbols/data"
repo_path="material-symbols"
repo="https://github.com/beecho01/${repo_path}"
if ! test -d ${base_repo_dir}; then
  echo "${base_repo_dir} folder does not exist, creating now..."
  mkdir ${base_repo_dir};
fi

cd ${base_repo_dir}
echo "CD into ${PWD}"