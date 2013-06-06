; 脚本由 Inno Setup 脚本向导 生成！
; 有关创建 Inno Setup 脚本文件的详细资料请查阅帮助文档！

#define MyAppName "Download-Google_Voice"
#define MyAppVersion "1.0"
#define MyAppPublisher "pikipity"
#define MyAppURL "http://www.pikipity.github.io/"

[Setup]
; 注: AppId的值为单独标识该应用程序。
; 不要为其他安装程序使用相同的AppId值。
; (生成新的GUID，点击 工具|在IDE中生成GUID。)
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
; 注意: 不要在任何共享系统文件上使用“Flags: ignoreversion”

[Icons]
Name: "{group}\{cm:ProgramOnTheWeb,{#MyAppName}}"; Filename: "{#MyAppURL}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"

