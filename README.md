# NFCTagServer_SMARTTHINGS
A Server which uses HTML and Smarttthings API to control Smart Appliances with multiple NFC TAGS

A django Server is being used. When and NFC tag is Triggered user is sent to the LOCAL Server, which in turn is this server. This server than checks the "key" =command and sees the data, with respect to the data, the respected Smart Appliance is controlled using the SMARTTHINGS API.
