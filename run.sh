PYTHON_SCRIPT_PATH=
VENV_PATH=

source $VENV_PATH/bin/activate

if [ -f "$PYTHON_SCRIPT_PATH" ]; then
    echo "Python script found: $PYTHON_SCRIPT_PATH"
fi

python3 $PYTHON_SCRIPT_PATH

if [ $? -eq 0 ]; then
    echo "Python script executed successfully."
else
    echo "Python script execution failed."
    exit 1
fi

deactivate