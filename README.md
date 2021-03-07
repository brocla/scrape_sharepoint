# scrape_sharepoint

An example script that shows how to:

Scrape a SharePoint to get a data List, using a Windows machine, in a corporate environment.

Combines the authentication from [requests_negotiate_sspi](https://pypi.org/project/requests-negotiate-sspi/) and the scraping tools of [SharePlum](https://pypi.org/project/SharePlum/)

- **requests-negotiate-sspi** allows for Single-Sign On HTTP Negotiate authentication using the requests library on Windows.
- **SharePlum** is an easy framework to work with SharePoint services.

The authorization only works on Windows machines.

It does not try to defeat the security. If you don't have authorization for the SharePoint, this won't help.

To do more with SharePlum than just connect, strongly recommend the well written [Read the Docs](https://shareplum.readthedocs.io/en/latest/)
