base_repo_dir=raw2
base_files_dir="/custom_components/material_symbols/data"
repo_path="material-symbols"
repo="https://github.com/beecho01/${repo_path}"
if ! test -d ${base_repo_dir}; then
  echo "${base_repo_dir} folder does not exist, creating now..."
  echo ""
  mkdir ${base_repo_dir};
fi

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