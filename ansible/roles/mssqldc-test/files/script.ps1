Import-Module 'C:\Program Files\Pure Storage\D.O.E.S\DOES.Powershell.dll'

Add-DataEngine -DatabaseType MicrosoftSQL -Hostname localhost -DatabaseName db1 -Amount 1 -Unit Terabytes -NumberOfThreads 8 -UserName admin -Password VMware1! -Folder Z:\packages\datafiles\DataEngineFilesOracle1
