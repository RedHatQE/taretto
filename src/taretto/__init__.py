from apipkg import initpkg as __initpkg

# fmt: off
__initpkg(__name__, {
    "navigate": "navmazing",
    "ui": {
        "core": "widgetastic.widget",  # todo: html widget library here, limit to base
        "patternfly": "widgetastic_patternfly",  # dito
        "patternfly4": "widgetastic_patternfly4",

        "View": "widgetastic.widget:View",
        "Browser": "widgetastic.browser:Browser",
        "DefaultPlugin": "widgetastic.browser:DefaultPlugin"
    },
})
