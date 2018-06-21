from apipkg import initpkg as __initpkg

# fmt: off
__initpkg(__name__, {
    "navigate": "navmazing",
    "ui": {
        "core": "widgetastic.widget",  # todo: html widget library here, limit to base
        "patternfly": "widgetastic.patternfly",  # dito

        "View": "widgetastic.widget:View",
        "Browser": "widgetastic.browser.Browser",
    },
})
