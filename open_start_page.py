dict(id="6fed5b59-7e38-45f9-a284-376f8cb796e1", version="2.0", name="Training", url="https://fix.sbis.ru", tests=[{
  "id": "a09bd395-d411-4741-a262-d2c6bde81759",
  "name": "open_start_page",
  "commands": [{
    "id": "980d9835-ed7a-4311-83e8-3b08366c27ce",
    "comment": "",
    "command": "open",
    "target": "/",
    "targets": [],
    "value": ""
  }, {
    "id": "db5cc029-eddf-4711-a56d-fb3096dcdc37",
    "comment": "",
    "command": "setWindowSize",
    "target": "1936x1056",
    "targets": [],
    "value": ""
  }, {
    "id": "bde91f8a-42e9-402c-a683-e4609574c3a3",
    "comment": "",
    "command": "click",
    "target": "css=.sbis_ru-menu__item-wrap:nth-child(9) .sbis_ru-menu__caption",
    "targets": [
      ["css=.sbis_ru-menu__item-wrap:nth-child(9) .sbis_ru-menu__caption", "css:finder"],
      ["xpath=//div[@id='ws-nrbolxhhrd1601659179538']/ul/li[9]/a/span[2]", "xpath:idRelative"],
      ["xpath=//li[9]/a/span[2]", "xpath:position"]
    ],
    "value": ""
  }, {
    "id": "1d510699-2eb6-41a2-ba7d-687af81f37e0",
    "comment": "",
    "command": "runScript",
    "target": "window.scrollTo(0,0)",
    "targets": [],
    "value": ""
  }]
}], suites=[{
  "id": "2b543940-212a-444e-9a64-31ae2e2f15a6",
  "name": "Default Suite",
  "timeout": 300,
  "tests": ["a09bd395-d411-4741-a262-d2c6bde81759"]
}], urls=["https://fix.sbis.ru/"], plugins=[])
