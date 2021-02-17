pushd './${{ env.AZURE_FUNCTIONAPP_PACKAGE_PATH }}'
python -m pip install --upgrade pip
pip install -r requirements.txt --target=".python_packages/lib/site-packages"
popd
