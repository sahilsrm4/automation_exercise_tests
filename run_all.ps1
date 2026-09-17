# 1. Create the virtual environment if it doesn't exist
if (-not (Test-Path -Path ".venv")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Cyan
    python -m venv .venv
} else {
    Write-Host "Virtual environment already exists." -ForegroundColor Green
}

# 2. Activate the virtual environment for this script session
Write-Host "Activating virtual environment..." -ForegroundColor Cyan
.venv\Scripts\Activate.ps1

# 3. Upgrade pip and install all project dependencies
Write-Host "Installing dependencies from requirements.txt..." -ForegroundColor Cyan
python -m pip install --upgrade pip
pip install -r requirements.txt

# 4. Install Playwright browser drivers (skips automatically if already installed)
Write-Host "Installing Playwright browser drivers..." -ForegroundColor Cyan
playwright install

# 5. Run the pytest tests in headed mode
Write-Host "Running tests..." -ForegroundColor Green
pytest --headed
