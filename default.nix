with (import <nixpkgs> {});

mkShell {
  buildInputs = with pkgs; [
    python3Full
    python312Packages.pillow
    python312Packages.numpy
    python312Packages.wand
    python3Packages.venvShellHook
  ];
  venvDir = "./.venv";
  postVenvCreation = ''
    unset SOURCE_DATE_EPOCH
  '';
  postShellHook = ''
    unset SOURCE_DATE_EPOCH
  '';
}
