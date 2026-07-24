[CmdletBinding()]
param(
    [ValidateSet('all', 'paper1', 'paper2')]
    [string]$Paper = 'all'
)

$ErrorActionPreference = 'Stop'
$RepositoryRoot = $PSScriptRoot

function Build-Paper {
    param(
        [Parameter(Mandatory)]
        [string]$Directory,
        [Parameter(Mandatory)]
        [string]$PdfName
    )

    $PaperDirectory = Join-Path $RepositoryRoot $Directory
    $BuildDirectory = Join-Path $PaperDirectory 'build'
    New-Item -ItemType Directory -Force -Path $BuildDirectory | Out-Null

    Push-Location $PaperDirectory
    try {
        $Tectonic = Get-Command tectonic -ErrorAction SilentlyContinue
        if ($Tectonic) {
            & $Tectonic.Source -X compile --outdir $BuildDirectory main.tex
        }
        else {
            $Latexmk = Get-Command latexmk -ErrorAction SilentlyContinue
            if (-not $Latexmk) {
                throw 'Install Tectonic or latexmk before building the papers.'
            }
            & $Latexmk.Source -pdf -interaction=nonstopmode -halt-on-error `
                -outdir=$BuildDirectory main.tex
        }

        $BuiltPdf = Join-Path $BuildDirectory 'main.pdf'
        if (-not (Test-Path -LiteralPath $BuiltPdf)) {
            throw "Expected PDF was not created: $BuiltPdf"
        }
        Copy-Item -LiteralPath $BuiltPdf `
            -Destination (Join-Path $PaperDirectory $PdfName) -Force
        Copy-Item -LiteralPath $BuiltPdf `
            -Destination (Join-Path $RepositoryRoot "output\pdf\$PdfName") -Force
    }
    finally {
        Pop-Location
    }
}

if ($Paper -in @('all', 'paper1')) {
    Build-Paper `
        -Directory 'papers\paper-1-selected-channel-entropy' `
        -PdfName 'siraji_selected_channel_entropy_failure.pdf'
}

if ($Paper -in @('all', 'paper2')) {
    Build-Paper `
        -Directory 'papers\paper-2-operator-valued-riesz' `
        -PdfName 'siraji_operator_valued_riesz_contraction.pdf'
}
