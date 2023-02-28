type nul > %ARTICLE_URLS_FILE%
for %%i in (out\*) do (
    if %%~nxi NEQ %OUT_DIR_BASE_FILE% (
        echo %%~nxi >> %ARTICLE_URLS_FILE%
    )
)
python pocket_upload.py %CUSTOM_WEBSITE% %ARTICLE_URLS_FILE% %ACCESS_TOKEN% %CONSUMER_KEY% %ARTICLE_NAMES_FILE%

exit 0
