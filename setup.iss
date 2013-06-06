; �ű��� Inno Setup �ű��� ���ɣ�
; �йش��� Inno Setup �ű��ļ�����ϸ��������İ����ĵ���

#define MyAppName "Download-Google_Voice"
#define MyAppVersion "1.0"
#define MyAppPublisher "pikipity"
#define MyAppURL "http://www.pikipity.github.io/"

[Setup]
; ע: AppId��ֵΪ������ʶ��Ӧ�ó���
; ��ҪΪ������װ����ʹ����ͬ��AppIdֵ��
; (�����µ�GUID����� ����|��IDE������GUID��)
AppId={{8778F480-0654-4280-99AD-6A604A16AD60}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\Download_Google_Voice
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
LicenseFile=C:\Documents and Settings\Administrator\My Documents\GitHub\Download-Google-Voice\dist\License.txt
InfoBeforeFile=C:\Documents and Settings\Administrator\My Documents\GitHub\Download-Google-Voice\README.txt
InfoAfterFile=C:\Documents and Settings\Administrator\My Documents\GitHub\Download-Google-Voice\Final information.txt
OutputDir=C:\Documents and Settings\Administrator\My Documents\GitHub\Download-Google-Voice
OutputBaseFilename=setup
SetupIconFile=C:\Documents and Settings\Administrator\My Documents\GitHub\Download-Google-Voice\dist\icon\Voice.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Languages\English.isl"

[Files]
Source: "C:\Documents and Settings\Administrator\My Documents\GitHub\Download-Google-Voice\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; ע��: ��Ҫ���κι���ϵͳ�ļ���ʹ�á�Flags: ignoreversion��

[Icons]
Name: "{group}\{cm:ProgramOnTheWeb,{#MyAppName}}"; Filename: "{#MyAppURL}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"

