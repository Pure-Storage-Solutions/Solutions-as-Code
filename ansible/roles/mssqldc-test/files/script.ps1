Import-Module 'C:\Program Files\Pure Storage\D.O.E.S\DOES.Powershell.dll'

Add-DataEngine -DatabaseType MicrosoftSQL -DatabaseName db1 -Amount 500 -Unit Gigabytes -NumberOfThreads 4 -UserName administrator -Password VMware1!
