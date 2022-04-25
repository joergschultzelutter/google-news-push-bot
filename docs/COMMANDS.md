# Command line parameters

The following section describes the command line parameters which can be used to influence the program's behavior. In addition to these parameters, settings such as the watch area(s) are configured in the program's config file - see separate section.

    usage: gnpush.py [-h] [--topics TOPICS] [--messengers MESSENGERS] [--run-interval RUN_INTERVAL] [--age AGE] [--msg-buffer-size MSG_BUFFER_SIZE]
    				 [--generate-test-message] [--ttl TIME_TO_LIVE]

## Optional command line parameters

- ``topics`` Name of the search topics configuration YAML file. Default is '__gnpush_topics.yml__'
- ``messengers`` Name of the Apprise messenger configuration YAML file. Default is '__gnpush_messengers.yml__'
- ``run-interval`` Run interval in hours (e.g. run every x hours). Default is '__24__' (hours)
- ``age`` max. age of the article on Google News in days. Default is '__7__' (days)
- ``msg-buffer-size`` Size of the expiring dictionary (read: how many URLs will be stored). Default is '__1000__' (entries)
- ``generate_test_message`` Default value is ``False``. If you set this value to ``True``, the program will start up as usual but will send only _one_ test message to your Apprise account(s). Once this data was sent to the respective APIs, the program will exit.
- ``ttl`` max. age of the article in our expiring dictionary. Default is '__7__' (days). Within that time span, the article URL will not be sent to the user again (unless you restart the program)
