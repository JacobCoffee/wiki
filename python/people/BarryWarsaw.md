# BarryWarsaw

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

![](http://www.python.org/~guido/pycon03/PyCon/thumbs/P3260137-THUMB.JPG "http://www.python.org/~guido/pycon03/PyCon/thumbs/P3260137-THUMB.JPG")

BarryWarsaw has his home page at [http://barry.warsaw.us/](http://barry.warsaw.us/)

## Some useful Emacs stuff for Python hacking 

    (require 'flymake)

    ;; Redefine this to shorten the mode-line real-estate.
    (defun flymake-report-status (e-w &optional status)
      "Show status in mode line."
      (when e-w
        (setq flymake-mode-line-e-w e-w))
      (when status
        (setq flymake-mode-line-status status))
      (let* ((mode-line " FM"))             ;BAW 2010-10-08
        (when (> (length flymake-mode-line-e-w) 0)
          (setq mode-line (concat mode-line ":" flymake-mode-line-e-w)))
        (setq mode-line (concat mode-line flymake-mode-line-status))
        (setq flymake-mode-line mode-line)
        (force-mode-line-update)))

    (defun baw-flymake-pyflakes-init ()
      (let* ((temp-file (flymake-init-create-temp-buffer-copy
                         'flymake-create-temp-inplace))
             (local-file (file-relative-name
                          temp-file
                          (file-name-directory buffer-file-name))))
        (list "pyflakes" (list local-file))))
    ;; For now, only flymake on Python files.
    (setq flymake-allowed-file-name-masks
          '(("\\.py\\'" baw-flymake-pyflakes-init)))
    (add-hook 'find-file-hook 'flymake-find-file-hook)
    (global-set-key [(control c) (meta n)] 'flymake-goto-next-error)
    (global-set-key [(control c) (meta p)] 'flymake-goto-prev-error)
    (global-set-key [(control c) (meta e)]
                    'flymake-display-err-menu-for-current-line)

    (defun baw-python-mode-hook ()
      (setq comment-column 50
            fill-column 78)
      (setq mode-name "Py")
      (flyspell-prog-mode)
      (define-key python-mode-map [(meta f)] 'py-forward-into-nomenclature)
      (define-key python-mode-map [(meta b)] 'py-backward-into-nomenclature))
    (add-hook 'python-mode-hook 'baw-python-mode-hook)

------------------------------------------------------------------------

[CategoryHomepage](CategoryHomepage)
