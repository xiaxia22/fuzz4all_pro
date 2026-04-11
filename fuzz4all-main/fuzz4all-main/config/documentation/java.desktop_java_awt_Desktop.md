# Class Desktop

**Source:** `java.desktop\java\awt\Desktop.html`

### Class Description

```java
public class
Desktop

extends
Object
```

The

Desktop

class allows interact with various desktop capabilities.

Supported operations include:

- launching the user-default browser to show a specified
URI;
- launching the user-default mail client with an optional

mailto

URI;
- launching a registered application to open, edit or print a
specified file.

This class provides methods corresponding to these
operations. The methods look for the associated application
registered on the current platform, and launch it to handle a URI
or file. If there is no associated application or the associated
application fails to be launched, an exception is thrown.

Please see

Desktop.Action

for the full list of supported operations
and capabilities.

An application is registered to a URI or file type.
The mechanism of registering, accessing, and
launching the associated application is platform-dependent.

Each operation is an action type represented by the

Desktop.Action

class.

Note: when some action is invoked and the associated
application is executed, it will be executed on the same system as
the one on which the Java application was launched.

**Since:** 1.6
**See Also:** Desktop.Action

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Desktop
getDesktop()

Returns the

Desktop

instance of the current
desktop context. On some platforms the Desktop API may not be
supported; use the

isDesktopSupported()

method to
determine if the current desktop is supported.

**Returns:**
- the Desktop instance

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
- UnsupportedOperationException

- if this class is not
supported on the current platform

**See Also:**
- isDesktopSupported()

,

GraphicsEnvironment.isHeadless()

---

#### public static boolean isDesktopSupported()

Tests whether this class is supported on the current platform.
If it's supported, use

getDesktop()

to retrieve an
instance.

**Returns:**
- true

if this class is supported on the
current platform;

false

otherwise

**See Also:**
- getDesktop()

---

#### public boolean isSupported​(
Desktop.Action
action)

Tests whether an action is supported on the current platform.

Even when the platform supports an action, a file or URI may
not have a registered application for the action. For example,
most of the platforms support the

Desktop.Action.OPEN

action. But for a specific file, there may not be an
application registered to open it. In this case,

isSupported(Action)

may return

true

, but the corresponding
action method will throw an

IOException

.

**Parameters:**
- action

- the specified

Desktop.Action

**Returns:**
- true

if the specified action is supported on
the current platform;

false

otherwise

**See Also:**
- Desktop.Action

---

#### public void open​(
File
file)
throws
IOException

Launches the associated application to open the file.

If the specified file is a directory, the file manager of
the current platform is launched to open it.

**Parameters:**
- file

- the file to be opened with the associated application

**Throws:**
- NullPointerException

- if

file

is

null
- IllegalArgumentException

- if the specified file doesn't
exist
- UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.OPEN

action
- IOException

- if the specified file has no associated
application or the associated application fails to be launched
- SecurityException

- if a security manager exists and its

SecurityManager.checkRead(java.lang.String)

method denies read access to the file, or it denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess

**See Also:**
- AWTPermission

---

#### public void edit​(
File
file)
throws
IOException

Launches the associated editor application and opens a file for
editing.

**Parameters:**
- file

- the file to be opened for editing

**Throws:**
- NullPointerException

- if the specified file is

null
- IllegalArgumentException

- if the specified file doesn't
exist
- UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.EDIT

action
- IOException

- if the specified file has no associated
editor, or the associated application fails to be launched
- SecurityException

- if a security manager exists and its

SecurityManager.checkRead(java.lang.String)

method denies read access to the file, or

SecurityManager.checkWrite(java.lang.String)

method
denies write access to the file, or it denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess

**See Also:**
- AWTPermission

---

#### public void print​(
File
file)
throws
IOException

Prints a file with the native desktop printing facility, using
the associated application's print command.

**Parameters:**
- file

- the file to be printed

**Throws:**
- NullPointerException

- if the specified file is

null
- IllegalArgumentException

- if the specified file doesn't
exist
- UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.PRINT

action
- IOException

- if the specified file has no associated
application that can be used to print it
- SecurityException

- if a security manager exists and its

SecurityManager.checkRead(java.lang.String)

method denies read access to the file, or its

SecurityManager.checkPrintJobAccess()

method denies
the permission to print the file, or the calling thread is not
allowed to create a subprocess

---

#### public void browse​(
URI
uri)
throws
IOException

Launches the default browser to display a

URI

.
If the default browser is not able to handle the specified

URI

, the application registered for handling

URIs

of the specified type is invoked. The application
is determined from the protocol and path of the

URI

, as
defined by the

URI

class.

**Parameters:**
- uri

- the URI to be displayed in the user default browser

**Throws:**
- NullPointerException

- if

uri

is

null
- UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.BROWSE

action
- IOException

- if the user default browser is not found,
or it fails to be launched, or the default handler application
failed to be launched
- SecurityException

- if a security manager exists and it
denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess

**See Also:**
- URI

,

AWTPermission

---

#### public void mail()
throws
IOException

Launches the mail composing window of the user default mail
client.

**Throws:**
- UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.MAIL

action
- IOException

- if the user default mail client is not
found, or it fails to be launched
- SecurityException

- if a security manager exists and it
denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess

**See Also:**
- AWTPermission

---

#### public void mail​(
URI
mailtoURI)
throws
IOException

Launches the mail composing window of the user default mail
client, filling the message fields specified by a

mailto:

URI.

A

mailto:

URI can specify message fields
including

"to"

,

"cc"

,

"subject"

,

"body"

, etc. See

The mailto URL
scheme (RFC 2368)

for the

mailto:

URI specification
details.

**Parameters:**
- mailtoURI

- the specified

mailto:

URI

**Throws:**
- NullPointerException

- if the specified URI is

null
- IllegalArgumentException

- if the URI scheme is not

"mailto"
- UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.MAIL

action
- IOException

- if the user default mail client is not
found or fails to be launched
- SecurityException

- if a security manager exists and it
denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess

**See Also:**
- URI

,

AWTPermission

---

#### public void addAppEventListener​(
SystemEventListener
listener)

Adds sub-types of

SystemEventListener

to listen for notifications
from the native system.

Has no effect if SystemEventListener's sub-type is unsupported on the current
platform.

**Parameters:**
- listener

- listener

**Throws:**
- SecurityException

- if a security manager exists and it
denies the

RuntimePermission("canProcessApplicationEvents")

permission

**See Also:**
- AppForegroundListener

,

AppHiddenListener

,

AppReopenedListener

,

ScreenSleepListener

,

SystemSleepListener

,

UserSessionListener

**Since:**
- 9

---

#### public void removeAppEventListener​(
SystemEventListener
listener)

Removes sub-types of

SystemEventListener

to listen for notifications
from the native system.

Has no effect if SystemEventListener's sub-type is unsupported on the current
platform.

**Parameters:**
- listener

- listener

**Throws:**
- SecurityException

- if a security manager exists and it
denies the

RuntimePermission("canProcessApplicationEvents")

permission

**See Also:**
- AppForegroundListener

,

AppHiddenListener

,

AppReopenedListener

,

ScreenSleepListener

,

SystemSleepListener

,

UserSessionListener

**Since:**
- 9

---

#### public void setAboutHandler​(
AboutHandler
aboutHandler)

Installs a handler to show a custom About window for your application.

Setting the

AboutHandler

to

null

reverts it to the
default behavior.

**Parameters:**
- aboutHandler

- the handler to respond to the

AboutHandler.handleAbout(AboutEvent)

message

**Throws:**
- SecurityException

- if a security manager exists and it
denies the

RuntimePermission("canProcessApplicationEvents")

permission
- UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_ABOUT

action

**Since:**
- 9

---

#### public void setPreferencesHandler​(
PreferencesHandler
preferencesHandler)

Installs a handler to show a custom Preferences window for your
application.

Setting the

PreferencesHandler

to

null

reverts it to
the default behavior

**Parameters:**
- preferencesHandler

- the handler to respond to the

PreferencesHandler.handlePreferences(PreferencesEvent)

**Throws:**
- SecurityException

- if a security manager exists and it
denies the

RuntimePermission("canProcessApplicationEvents")

permission
- UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_PREFERENCES

action

**Since:**
- 9

---

#### public void setOpenFileHandler​(
OpenFilesHandler
openFileHandler)

Installs the handler which is notified when the application is asked to
open a list of files.

**Parameters:**
- openFileHandler

- handler

**Throws:**
- SecurityException

- if a security manager exists and its

SecurityManager.checkRead(java.lang.String)

method denies read access to the files, or it denies the

RuntimePermission("canProcessApplicationEvents")

permission, or the calling thread is not allowed to create a
subprocess
- UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_OPEN_FILE

action

**Since:**
- 9

**Implementation Note:**
- Please note that for macOS, notifications
are only sent if the Java app is a bundled application,
with a

CFBundleDocumentTypes

array present in its

Info.plist

. Check the

Apple Developer Documentation

for more information about

Info.plist

.

---

#### public void setPrintFileHandler​(
PrintFilesHandler
printFileHandler)

Installs the handler which is notified when the application is asked to
print a list of files.

**Parameters:**
- printFileHandler

- handler

**Throws:**
- SecurityException

- if a security manager exists and its

SecurityManager.checkPrintJobAccess()

method denies
the permission to print or it denies the

RuntimePermission("canProcessApplicationEvents")

permission
- UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_PRINT_FILE

action

**Since:**
- 9

**Implementation Note:**
- Please note that for macOS, notifications
are only sent if the Java app is a bundled application,
with a

CFBundleDocumentTypes

array present in its

Info.plist

. Check the

Apple Developer Documentation

for more information about

Info.plist

.

---

#### public void setOpenURIHandler​(
OpenURIHandler
openURIHandler)

Installs the handler which is notified when the application is asked to
open a URL.

Setting the handler to

null

causes all

OpenURIHandler.openURI(OpenURIEvent)

requests to be
enqueued until another handler is set.

**Parameters:**
- openURIHandler

- handler

RuntimePermission("canProcessApplicationEvents")

permission, or the calling thread is not allowed to create a
subprocess

**Throws:**
- UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_OPEN_URI

action

**Since:**
- 9

**Implementation Note:**
- Please note that for macOS, notifications
are only sent if the Java app is a bundled application,
with a

CFBundleDocumentTypes

array present in its

Info.plist

. Check the

Apple Developer Documentation

for more information about

Info.plist

.

---

#### public void setQuitHandler​(
QuitHandler
quitHandler)

Installs the handler which determines if the application should quit. The
handler is passed a one-shot

QuitResponse

which can cancel or
proceed with the quit. Setting the handler to

null

causes
all quit requests to directly perform the default

QuitStrategy

.

**Parameters:**
- quitHandler

- the handler that is called when the application is
asked to quit

**Throws:**
- SecurityException

- if a security manager exists and it
will not allow the caller to invoke

System.exit

or it denies the

RuntimePermission("canProcessApplicationEvents")

permission
- UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_QUIT_HANDLER

action

**Since:**
- 9

---

#### public void setQuitStrategy​(
QuitStrategy
strategy)

Sets the default strategy used to quit this application. The default is
calling SYSTEM_EXIT_0.

**Parameters:**
- strategy

- the way this application should be shutdown

**Throws:**
- SecurityException

- if a security manager exists and it
will not allow the caller to invoke

System.exit

or it denies the

RuntimePermission("canProcessApplicationEvents")

permission
- UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_QUIT_STRATEGY

action

**See Also:**
- QuitStrategy

**Since:**
- 9

---

#### public void enableSuddenTermination()

Enables this application to be suddenly terminated.

Call this method to indicate your application's state is saved, and
requires no notification to be terminated. Letting your application
remain terminatable improves the user experience by avoiding re-paging in
your application when it's asked to quit.

Note: enabling sudden termination will allow your application to be
quit without notifying your QuitHandler, or running any shutdown
hooks.

E.g. user-initiated Cmd-Q, logout, restart, or shutdown requests will
effectively "kill -KILL" your application.

**Throws:**
- SecurityException

- if a security manager exists and it
will not allow the caller to invoke

System.exit

or it denies the

RuntimePermission("canProcessApplicationEvents")

permission
- UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_SUDDEN_TERMINATION

action

**See Also:**
- disableSuddenTermination()

**Since:**
- 9

---

#### public void disableSuddenTermination()

Prevents this application from being suddenly terminated.

Call this method to indicate that your application has unsaved state, and
may not be terminated without notification.

**Throws:**
- SecurityException

- if a security manager exists and it
will not allow the caller to invoke

System.exit

or it denies the

RuntimePermission("canProcessApplicationEvents")

permission
- UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_SUDDEN_TERMINATION

action

**See Also:**
- enableSuddenTermination()

**Since:**
- 9

---

#### public void requestForeground​(boolean allWindows)

Requests this application to move to the foreground.

**Parameters:**
- allWindows

- if all windows of this application should be moved to
the foreground, or only the foremost one

**Throws:**
- SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
- UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_REQUEST_FOREGROUND

action

**Since:**
- 9

---

#### public void openHelpViewer()

Opens the native help viewer application.

**Throws:**
- SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission, or it denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
- UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_HELP_VIEWER

action

**Since:**
- 9

**Implementation Note:**
- Please note that for Mac OS, it opens the native help viewer
application if a Help Book has been added to the application bundler
and registered in the Info.plist with CFBundleHelpBookFolder

---

#### public void setDefaultMenuBar​(
JMenuBar
menuBar)

Sets the default menu bar to use when there are no active frames.

**Parameters:**
- menuBar

- to use when no other frames are active

**Throws:**
- SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
- UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_MENU_BAR

action

**Since:**
- 9

---

#### public void browseFileDirectory​(
File
file)

Opens a folder containing the

file

and selects it
in a default system file manager.

**Parameters:**
- file

- the file

**Throws:**
- SecurityException

- If a security manager exists and its

SecurityManager.checkRead(java.lang.String)

method
denies read access to the file or to its parent, or it denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
- UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.BROWSE_FILE_DIR

action
- NullPointerException

- if

file

is

null
- IllegalArgumentException

- if the specified file or its parent
doesn't exist

**Since:**
- 9

---

#### public boolean moveToTrash​(
File
file)

Moves the specified file to the trash.

**Parameters:**
- file

- the file

**Returns:**
- returns true if successfully moved the file to the trash.

**Throws:**
- SecurityException

- If a security manager exists and its

SecurityManager.checkDelete(java.lang.String)

method
denies deletion of the file
- UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.MOVE_TO_TRASH

action
- NullPointerException

- if

file

is

null
- IllegalArgumentException

- if the specified file doesn't exist

**Since:**
- 9

---

### Additional Sections

#### Class Desktop

java.lang.Object

- java.awt.Desktop

java.awt.Desktop

```java
public class
Desktop

extends
Object
```

The

Desktop

class allows interact with various desktop capabilities.

Supported operations include:

- launching the user-default browser to show a specified
URI;
- launching the user-default mail client with an optional

mailto

URI;
- launching a registered application to open, edit or print a
specified file.

This class provides methods corresponding to these
operations. The methods look for the associated application
registered on the current platform, and launch it to handle a URI
or file. If there is no associated application or the associated
application fails to be launched, an exception is thrown.

Please see

Desktop.Action

for the full list of supported operations
and capabilities.

An application is registered to a URI or file type.
The mechanism of registering, accessing, and
launching the associated application is platform-dependent.

Each operation is an action type represented by the

Desktop.Action

class.

Note: when some action is invoked and the associated
application is executed, it will be executed on the same system as
the one on which the Java application was launched.

**Since:** 1.6
**See Also:** Desktop.Action

public class

Desktop

extends

Object

The

Desktop

class allows interact with various desktop capabilities.

Supported operations include:

- launching the user-default browser to show a specified
URI;
- launching the user-default mail client with an optional

mailto

URI;
- launching a registered application to open, edit or print a
specified file.

This class provides methods corresponding to these
operations. The methods look for the associated application
registered on the current platform, and launch it to handle a URI
or file. If there is no associated application or the associated
application fails to be launched, an exception is thrown.

Please see

Desktop.Action

for the full list of supported operations
and capabilities.

An application is registered to a URI or file type.
The mechanism of registering, accessing, and
launching the associated application is platform-dependent.

Each operation is an action type represented by the

Desktop.Action

class.

Note: when some action is invoked and the associated
application is executed, it will be executed on the same system as
the one on which the Java application was launched.

Supported operations include:

- launching the user-default browser to show a specified
URI;
- launching the user-default mail client with an optional

mailto

URI;
- launching a registered application to open, edit or print a
specified file.

This class provides methods corresponding to these
operations. The methods look for the associated application
registered on the current platform, and launch it to handle a URI
or file. If there is no associated application or the associated
application fails to be launched, an exception is thrown.

Please see

Desktop.Action

for the full list of supported operations
and capabilities.

An application is registered to a URI or file type.
The mechanism of registering, accessing, and
launching the associated application is platform-dependent.

Each operation is an action type represented by the

Desktop.Action

class.

Note: when some action is invoked and the associated
application is executed, it will be executed on the same system as
the one on which the Java application was launched.

launching the user-default browser to show a specified
URI;

launching the user-default mail client with an optional

mailto

URI;

launching a registered application to open, edit or print a
specified file.

This class provides methods corresponding to these
operations. The methods look for the associated application
registered on the current platform, and launch it to handle a URI
or file. If there is no associated application or the associated
application fails to be launched, an exception is thrown.

Please see

Desktop.Action

for the full list of supported operations
and capabilities.

An application is registered to a URI or file type.
The mechanism of registering, accessing, and
launching the associated application is platform-dependent.

Each operation is an action type represented by the

Desktop.Action

class.

Note: when some action is invoked and the associated
application is executed, it will be executed on the same system as
the one on which the Java application was launched.

An application is registered to a URI or file type.
The mechanism of registering, accessing, and
launching the associated application is platform-dependent.

Each operation is an action type represented by the

Desktop.Action

class.

Note: when some action is invoked and the associated
application is executed, it will be executed on the same system as
the one on which the Java application was launched.

Each operation is an action type represented by the

Desktop.Action

class.

Note: when some action is invoked and the associated
application is executed, it will be executed on the same system as
the one on which the Java application was launched.

Note: when some action is invoked and the associated
application is executed, it will be executed on the same system as
the one on which the Java application was launched.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Desktop.Action

Represents an action type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addAppEventListener

​(

SystemEventListener

listener)

Adds sub-types of

SystemEventListener

to listen for notifications
from the native system.

void

browse

​(

URI

uri)

Launches the default browser to display a

URI

.

void

browseFileDirectory

​(

File

file)

Opens a folder containing the

file

and selects it
in a default system file manager.

void

disableSuddenTermination

()

Prevents this application from being suddenly terminated.

void

edit

​(

File

file)

Launches the associated editor application and opens a file for
editing.

void

enableSuddenTermination

()

Enables this application to be suddenly terminated.

static

Desktop

getDesktop

()

Returns the

Desktop

instance of the current
desktop context.

static boolean

isDesktopSupported

()

Tests whether this class is supported on the current platform.

boolean

isSupported

​(

Desktop.Action

action)

Tests whether an action is supported on the current platform.

void

mail

()

Launches the mail composing window of the user default mail
client.

void

mail

​(

URI

mailtoURI)

Launches the mail composing window of the user default mail
client, filling the message fields specified by a

mailto:

URI.

boolean

moveToTrash

​(

File

file)

Moves the specified file to the trash.

void

open

​(

File

file)

Launches the associated application to open the file.

void

openHelpViewer

()

Opens the native help viewer application.

void

print

​(

File

file)

Prints a file with the native desktop printing facility, using
the associated application's print command.

void

removeAppEventListener

​(

SystemEventListener

listener)

Removes sub-types of

SystemEventListener

to listen for notifications
from the native system.

void

requestForeground

​(boolean allWindows)

Requests this application to move to the foreground.

void

setAboutHandler

​(

AboutHandler

aboutHandler)

Installs a handler to show a custom About window for your application.

void

setDefaultMenuBar

​(

JMenuBar

menuBar)

Sets the default menu bar to use when there are no active frames.

void

setOpenFileHandler

​(

OpenFilesHandler

openFileHandler)

Installs the handler which is notified when the application is asked to
open a list of files.

void

setOpenURIHandler

​(

OpenURIHandler

openURIHandler)

Installs the handler which is notified when the application is asked to
open a URL.

void

setPreferencesHandler

​(

PreferencesHandler

preferencesHandler)

Installs a handler to show a custom Preferences window for your
application.

void

setPrintFileHandler

​(

PrintFilesHandler

printFileHandler)

Installs the handler which is notified when the application is asked to
print a list of files.

void

setQuitHandler

​(

QuitHandler

quitHandler)

Installs the handler which determines if the application should quit.

void

setQuitStrategy

​(

QuitStrategy

strategy)

Sets the default strategy used to quit this application.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Desktop.Action

Represents an action type.

---

#### Nested Class Summary

Represents an action type.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addAppEventListener

​(

SystemEventListener

listener)

Adds sub-types of

SystemEventListener

to listen for notifications
from the native system.

void

browse

​(

URI

uri)

Launches the default browser to display a

URI

.

void

browseFileDirectory

​(

File

file)

Opens a folder containing the

file

and selects it
in a default system file manager.

void

disableSuddenTermination

()

Prevents this application from being suddenly terminated.

void

edit

​(

File

file)

Launches the associated editor application and opens a file for
editing.

void

enableSuddenTermination

()

Enables this application to be suddenly terminated.

static

Desktop

getDesktop

()

Returns the

Desktop

instance of the current
desktop context.

static boolean

isDesktopSupported

()

Tests whether this class is supported on the current platform.

boolean

isSupported

​(

Desktop.Action

action)

Tests whether an action is supported on the current platform.

void

mail

()

Launches the mail composing window of the user default mail
client.

void

mail

​(

URI

mailtoURI)

Launches the mail composing window of the user default mail
client, filling the message fields specified by a

mailto:

URI.

boolean

moveToTrash

​(

File

file)

Moves the specified file to the trash.

void

open

​(

File

file)

Launches the associated application to open the file.

void

openHelpViewer

()

Opens the native help viewer application.

void

print

​(

File

file)

Prints a file with the native desktop printing facility, using
the associated application's print command.

void

removeAppEventListener

​(

SystemEventListener

listener)

Removes sub-types of

SystemEventListener

to listen for notifications
from the native system.

void

requestForeground

​(boolean allWindows)

Requests this application to move to the foreground.

void

setAboutHandler

​(

AboutHandler

aboutHandler)

Installs a handler to show a custom About window for your application.

void

setDefaultMenuBar

​(

JMenuBar

menuBar)

Sets the default menu bar to use when there are no active frames.

void

setOpenFileHandler

​(

OpenFilesHandler

openFileHandler)

Installs the handler which is notified when the application is asked to
open a list of files.

void

setOpenURIHandler

​(

OpenURIHandler

openURIHandler)

Installs the handler which is notified when the application is asked to
open a URL.

void

setPreferencesHandler

​(

PreferencesHandler

preferencesHandler)

Installs a handler to show a custom Preferences window for your
application.

void

setPrintFileHandler

​(

PrintFilesHandler

printFileHandler)

Installs the handler which is notified when the application is asked to
print a list of files.

void

setQuitHandler

​(

QuitHandler

quitHandler)

Installs the handler which determines if the application should quit.

void

setQuitStrategy

​(

QuitStrategy

strategy)

Sets the default strategy used to quit this application.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Adds sub-types of

SystemEventListener

to listen for notifications
from the native system.

Launches the default browser to display a

URI

.

Opens a folder containing the

file

and selects it
in a default system file manager.

Prevents this application from being suddenly terminated.

Launches the associated editor application and opens a file for
editing.

Enables this application to be suddenly terminated.

Returns the

Desktop

instance of the current
desktop context.

Tests whether this class is supported on the current platform.

Tests whether an action is supported on the current platform.

Launches the mail composing window of the user default mail
client.

Launches the mail composing window of the user default mail
client, filling the message fields specified by a

mailto:

URI.

Moves the specified file to the trash.

Launches the associated application to open the file.

Opens the native help viewer application.

Prints a file with the native desktop printing facility, using
the associated application's print command.

Removes sub-types of

SystemEventListener

to listen for notifications
from the native system.

Requests this application to move to the foreground.

Installs a handler to show a custom About window for your application.

Sets the default menu bar to use when there are no active frames.

Installs the handler which is notified when the application is asked to
open a list of files.

Installs the handler which is notified when the application is asked to
open a URL.

Installs a handler to show a custom Preferences window for your
application.

Installs the handler which is notified when the application is asked to
print a list of files.

Installs the handler which determines if the application should quit.

Sets the default strategy used to quit this application.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ METHOD DETAIL ==========

- Method Detail

- getDesktop

```java
public static
Desktop
getDesktop()
```

Returns the

Desktop

instance of the current
desktop context. On some platforms the Desktop API may not be
supported; use the

isDesktopSupported()

method to
determine if the current desktop is supported.

**Returns:** the Desktop instance
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** UnsupportedOperationException

- if this class is not
supported on the current platform
**See Also:** isDesktopSupported()

,

GraphicsEnvironment.isHeadless()

- isDesktopSupported

```java
public static boolean isDesktopSupported()
```

Tests whether this class is supported on the current platform.
If it's supported, use

getDesktop()

to retrieve an
instance.

**Returns:** true

if this class is supported on the
current platform;

false

otherwise
**See Also:** getDesktop()

- isSupported

```java
public boolean isSupported​(
Desktop.Action
action)
```

Tests whether an action is supported on the current platform.

Even when the platform supports an action, a file or URI may
not have a registered application for the action. For example,
most of the platforms support the

Desktop.Action.OPEN

action. But for a specific file, there may not be an
application registered to open it. In this case,

isSupported(Action)

may return

true

, but the corresponding
action method will throw an

IOException

.

**Parameters:** action

- the specified

Desktop.Action
**Returns:** true

if the specified action is supported on
the current platform;

false

otherwise
**See Also:** Desktop.Action

- open

```java
public void open​(
File
file)
throws
IOException
```

Launches the associated application to open the file.

If the specified file is a directory, the file manager of
the current platform is launched to open it.

**Parameters:** file

- the file to be opened with the associated application
**Throws:** NullPointerException

- if

file

is

null
**Throws:** IllegalArgumentException

- if the specified file doesn't
exist
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.OPEN

action
**Throws:** IOException

- if the specified file has no associated
application or the associated application fails to be launched
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkRead(java.lang.String)

method denies read access to the file, or it denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
**See Also:** AWTPermission

- edit

```java
public void edit​(
File
file)
throws
IOException
```

Launches the associated editor application and opens a file for
editing.

**Parameters:** file

- the file to be opened for editing
**Throws:** NullPointerException

- if the specified file is

null
**Throws:** IllegalArgumentException

- if the specified file doesn't
exist
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.EDIT

action
**Throws:** IOException

- if the specified file has no associated
editor, or the associated application fails to be launched
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkRead(java.lang.String)

method denies read access to the file, or

SecurityManager.checkWrite(java.lang.String)

method
denies write access to the file, or it denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
**See Also:** AWTPermission

- print

```java
public void print​(
File
file)
throws
IOException
```

Prints a file with the native desktop printing facility, using
the associated application's print command.

**Parameters:** file

- the file to be printed
**Throws:** NullPointerException

- if the specified file is

null
**Throws:** IllegalArgumentException

- if the specified file doesn't
exist
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.PRINT

action
**Throws:** IOException

- if the specified file has no associated
application that can be used to print it
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkRead(java.lang.String)

method denies read access to the file, or its

SecurityManager.checkPrintJobAccess()

method denies
the permission to print the file, or the calling thread is not
allowed to create a subprocess

- browse

```java
public void browse​(
URI
uri)
throws
IOException
```

Launches the default browser to display a

URI

.
If the default browser is not able to handle the specified

URI

, the application registered for handling

URIs

of the specified type is invoked. The application
is determined from the protocol and path of the

URI

, as
defined by the

URI

class.

**Parameters:** uri

- the URI to be displayed in the user default browser
**Throws:** NullPointerException

- if

uri

is

null
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.BROWSE

action
**Throws:** IOException

- if the user default browser is not found,
or it fails to be launched, or the default handler application
failed to be launched
**Throws:** SecurityException

- if a security manager exists and it
denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
**See Also:** URI

,

AWTPermission

- mail

```java
public void mail()
throws
IOException
```

Launches the mail composing window of the user default mail
client.

**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.MAIL

action
**Throws:** IOException

- if the user default mail client is not
found, or it fails to be launched
**Throws:** SecurityException

- if a security manager exists and it
denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
**See Also:** AWTPermission

- mail

```java
public void mail​(
URI
mailtoURI)
throws
IOException
```

Launches the mail composing window of the user default mail
client, filling the message fields specified by a

mailto:

URI.

A

mailto:

URI can specify message fields
including

"to"

,

"cc"

,

"subject"

,

"body"

, etc. See

The mailto URL
scheme (RFC 2368)

for the

mailto:

URI specification
details.

**Parameters:** mailtoURI

- the specified

mailto:

URI
**Throws:** NullPointerException

- if the specified URI is

null
**Throws:** IllegalArgumentException

- if the URI scheme is not

"mailto"
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.MAIL

action
**Throws:** IOException

- if the user default mail client is not
found or fails to be launched
**Throws:** SecurityException

- if a security manager exists and it
denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
**See Also:** URI

,

AWTPermission

- addAppEventListener

```java
public void addAppEventListener​(
SystemEventListener
listener)
```

Adds sub-types of

SystemEventListener

to listen for notifications
from the native system.

Has no effect if SystemEventListener's sub-type is unsupported on the current
platform.

**Parameters:** listener

- listener
**Throws:** SecurityException

- if a security manager exists and it
denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Since:** 9
**See Also:** AppForegroundListener

,

AppHiddenListener

,

AppReopenedListener

,

ScreenSleepListener

,

SystemSleepListener

,

UserSessionListener

- removeAppEventListener

```java
public void removeAppEventListener​(
SystemEventListener
listener)
```

Removes sub-types of

SystemEventListener

to listen for notifications
from the native system.

Has no effect if SystemEventListener's sub-type is unsupported on the current
platform.

**Parameters:** listener

- listener
**Throws:** SecurityException

- if a security manager exists and it
denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Since:** 9
**See Also:** AppForegroundListener

,

AppHiddenListener

,

AppReopenedListener

,

ScreenSleepListener

,

SystemSleepListener

,

UserSessionListener

- setAboutHandler

```java
public void setAboutHandler​(
AboutHandler
aboutHandler)
```

Installs a handler to show a custom About window for your application.

Setting the

AboutHandler

to

null

reverts it to the
default behavior.

**Parameters:** aboutHandler

- the handler to respond to the

AboutHandler.handleAbout(AboutEvent)

message
**Throws:** SecurityException

- if a security manager exists and it
denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_ABOUT

action
**Since:** 9

- setPreferencesHandler

```java
public void setPreferencesHandler​(
PreferencesHandler
preferencesHandler)
```

Installs a handler to show a custom Preferences window for your
application.

Setting the

PreferencesHandler

to

null

reverts it to
the default behavior

**Parameters:** preferencesHandler

- the handler to respond to the

PreferencesHandler.handlePreferences(PreferencesEvent)
**Throws:** SecurityException

- if a security manager exists and it
denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_PREFERENCES

action
**Since:** 9

- setOpenFileHandler

```java
public void setOpenFileHandler​(
OpenFilesHandler
openFileHandler)
```

Installs the handler which is notified when the application is asked to
open a list of files.

**Implementation Note:** Please note that for macOS, notifications
are only sent if the Java app is a bundled application,
with a

CFBundleDocumentTypes

array present in its

Info.plist

. Check the

Apple Developer Documentation

for more information about

Info.plist

.
**Parameters:** openFileHandler

- handler
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkRead(java.lang.String)

method denies read access to the files, or it denies the

RuntimePermission("canProcessApplicationEvents")

permission, or the calling thread is not allowed to create a
subprocess
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_OPEN_FILE

action
**Since:** 9

- setPrintFileHandler

```java
public void setPrintFileHandler​(
PrintFilesHandler
printFileHandler)
```

Installs the handler which is notified when the application is asked to
print a list of files.

**Implementation Note:** Please note that for macOS, notifications
are only sent if the Java app is a bundled application,
with a

CFBundleDocumentTypes

array present in its

Info.plist

. Check the

Apple Developer Documentation

for more information about

Info.plist

.
**Parameters:** printFileHandler

- handler
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkPrintJobAccess()

method denies
the permission to print or it denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_PRINT_FILE

action
**Since:** 9

- setOpenURIHandler

```java
public void setOpenURIHandler​(
OpenURIHandler
openURIHandler)
```

Installs the handler which is notified when the application is asked to
open a URL.

Setting the handler to

null

causes all

OpenURIHandler.openURI(OpenURIEvent)

requests to be
enqueued until another handler is set.

**Implementation Note:** Please note that for macOS, notifications
are only sent if the Java app is a bundled application,
with a

CFBundleDocumentTypes

array present in its

Info.plist

. Check the

Apple Developer Documentation

for more information about

Info.plist

.
**Parameters:** openURIHandler

- handler

RuntimePermission("canProcessApplicationEvents")

permission, or the calling thread is not allowed to create a
subprocess
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_OPEN_URI

action
**Since:** 9

- setQuitHandler

```java
public void setQuitHandler​(
QuitHandler
quitHandler)
```

Installs the handler which determines if the application should quit. The
handler is passed a one-shot

QuitResponse

which can cancel or
proceed with the quit. Setting the handler to

null

causes
all quit requests to directly perform the default

QuitStrategy

.

**Parameters:** quitHandler

- the handler that is called when the application is
asked to quit
**Throws:** SecurityException

- if a security manager exists and it
will not allow the caller to invoke

System.exit

or it denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_QUIT_HANDLER

action
**Since:** 9

- setQuitStrategy

```java
public void setQuitStrategy​(
QuitStrategy
strategy)
```

Sets the default strategy used to quit this application. The default is
calling SYSTEM_EXIT_0.

**Parameters:** strategy

- the way this application should be shutdown
**Throws:** SecurityException

- if a security manager exists and it
will not allow the caller to invoke

System.exit

or it denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_QUIT_STRATEGY

action
**Since:** 9
**See Also:** QuitStrategy

- enableSuddenTermination

```java
public void enableSuddenTermination()
```

Enables this application to be suddenly terminated.

Call this method to indicate your application's state is saved, and
requires no notification to be terminated. Letting your application
remain terminatable improves the user experience by avoiding re-paging in
your application when it's asked to quit.

Note: enabling sudden termination will allow your application to be
quit without notifying your QuitHandler, or running any shutdown
hooks.

E.g. user-initiated Cmd-Q, logout, restart, or shutdown requests will
effectively "kill -KILL" your application.

**Throws:** SecurityException

- if a security manager exists and it
will not allow the caller to invoke

System.exit

or it denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_SUDDEN_TERMINATION

action
**Since:** 9
**See Also:** disableSuddenTermination()

- disableSuddenTermination

```java
public void disableSuddenTermination()
```

Prevents this application from being suddenly terminated.

Call this method to indicate that your application has unsaved state, and
may not be terminated without notification.

**Throws:** SecurityException

- if a security manager exists and it
will not allow the caller to invoke

System.exit

or it denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_SUDDEN_TERMINATION

action
**Since:** 9
**See Also:** enableSuddenTermination()

- requestForeground

```java
public void requestForeground​(boolean allWindows)
```

Requests this application to move to the foreground.

**Parameters:** allWindows

- if all windows of this application should be moved to
the foreground, or only the foremost one
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_REQUEST_FOREGROUND

action
**Since:** 9

- openHelpViewer

```java
public void openHelpViewer()
```

Opens the native help viewer application.

**Implementation Note:** Please note that for Mac OS, it opens the native help viewer
application if a Help Book has been added to the application bundler
and registered in the Info.plist with CFBundleHelpBookFolder
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission, or it denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_HELP_VIEWER

action
**Since:** 9

- setDefaultMenuBar

```java
public void setDefaultMenuBar​(
JMenuBar
menuBar)
```

Sets the default menu bar to use when there are no active frames.

**Parameters:** menuBar

- to use when no other frames are active
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_MENU_BAR

action
**Since:** 9

- browseFileDirectory

```java
public void browseFileDirectory​(
File
file)
```

Opens a folder containing the

file

and selects it
in a default system file manager.

**Parameters:** file

- the file
**Throws:** SecurityException

- If a security manager exists and its

SecurityManager.checkRead(java.lang.String)

method
denies read access to the file or to its parent, or it denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.BROWSE_FILE_DIR

action
**Throws:** NullPointerException

- if

file

is

null
**Throws:** IllegalArgumentException

- if the specified file or its parent
doesn't exist
**Since:** 9

- moveToTrash

```java
public boolean moveToTrash​(
File
file)
```

Moves the specified file to the trash.

**Parameters:** file

- the file
**Returns:** returns true if successfully moved the file to the trash.
**Throws:** SecurityException

- If a security manager exists and its

SecurityManager.checkDelete(java.lang.String)

method
denies deletion of the file
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.MOVE_TO_TRASH

action
**Throws:** NullPointerException

- if

file

is

null
**Throws:** IllegalArgumentException

- if the specified file doesn't exist
**Since:** 9

Method Detail

- getDesktop

```java
public static
Desktop
getDesktop()
```

Returns the

Desktop

instance of the current
desktop context. On some platforms the Desktop API may not be
supported; use the

isDesktopSupported()

method to
determine if the current desktop is supported.

**Returns:** the Desktop instance
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** UnsupportedOperationException

- if this class is not
supported on the current platform
**See Also:** isDesktopSupported()

,

GraphicsEnvironment.isHeadless()

- isDesktopSupported

```java
public static boolean isDesktopSupported()
```

Tests whether this class is supported on the current platform.
If it's supported, use

getDesktop()

to retrieve an
instance.

**Returns:** true

if this class is supported on the
current platform;

false

otherwise
**See Also:** getDesktop()

- isSupported

```java
public boolean isSupported​(
Desktop.Action
action)
```

Tests whether an action is supported on the current platform.

Even when the platform supports an action, a file or URI may
not have a registered application for the action. For example,
most of the platforms support the

Desktop.Action.OPEN

action. But for a specific file, there may not be an
application registered to open it. In this case,

isSupported(Action)

may return

true

, but the corresponding
action method will throw an

IOException

.

**Parameters:** action

- the specified

Desktop.Action
**Returns:** true

if the specified action is supported on
the current platform;

false

otherwise
**See Also:** Desktop.Action

- open

```java
public void open​(
File
file)
throws
IOException
```

Launches the associated application to open the file.

If the specified file is a directory, the file manager of
the current platform is launched to open it.

**Parameters:** file

- the file to be opened with the associated application
**Throws:** NullPointerException

- if

file

is

null
**Throws:** IllegalArgumentException

- if the specified file doesn't
exist
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.OPEN

action
**Throws:** IOException

- if the specified file has no associated
application or the associated application fails to be launched
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkRead(java.lang.String)

method denies read access to the file, or it denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
**See Also:** AWTPermission

- edit

```java
public void edit​(
File
file)
throws
IOException
```

Launches the associated editor application and opens a file for
editing.

**Parameters:** file

- the file to be opened for editing
**Throws:** NullPointerException

- if the specified file is

null
**Throws:** IllegalArgumentException

- if the specified file doesn't
exist
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.EDIT

action
**Throws:** IOException

- if the specified file has no associated
editor, or the associated application fails to be launched
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkRead(java.lang.String)

method denies read access to the file, or

SecurityManager.checkWrite(java.lang.String)

method
denies write access to the file, or it denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
**See Also:** AWTPermission

- print

```java
public void print​(
File
file)
throws
IOException
```

Prints a file with the native desktop printing facility, using
the associated application's print command.

**Parameters:** file

- the file to be printed
**Throws:** NullPointerException

- if the specified file is

null
**Throws:** IllegalArgumentException

- if the specified file doesn't
exist
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.PRINT

action
**Throws:** IOException

- if the specified file has no associated
application that can be used to print it
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkRead(java.lang.String)

method denies read access to the file, or its

SecurityManager.checkPrintJobAccess()

method denies
the permission to print the file, or the calling thread is not
allowed to create a subprocess

- browse

```java
public void browse​(
URI
uri)
throws
IOException
```

Launches the default browser to display a

URI

.
If the default browser is not able to handle the specified

URI

, the application registered for handling

URIs

of the specified type is invoked. The application
is determined from the protocol and path of the

URI

, as
defined by the

URI

class.

**Parameters:** uri

- the URI to be displayed in the user default browser
**Throws:** NullPointerException

- if

uri

is

null
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.BROWSE

action
**Throws:** IOException

- if the user default browser is not found,
or it fails to be launched, or the default handler application
failed to be launched
**Throws:** SecurityException

- if a security manager exists and it
denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
**See Also:** URI

,

AWTPermission

- mail

```java
public void mail()
throws
IOException
```

Launches the mail composing window of the user default mail
client.

**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.MAIL

action
**Throws:** IOException

- if the user default mail client is not
found, or it fails to be launched
**Throws:** SecurityException

- if a security manager exists and it
denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
**See Also:** AWTPermission

- mail

```java
public void mail​(
URI
mailtoURI)
throws
IOException
```

Launches the mail composing window of the user default mail
client, filling the message fields specified by a

mailto:

URI.

A

mailto:

URI can specify message fields
including

"to"

,

"cc"

,

"subject"

,

"body"

, etc. See

The mailto URL
scheme (RFC 2368)

for the

mailto:

URI specification
details.

**Parameters:** mailtoURI

- the specified

mailto:

URI
**Throws:** NullPointerException

- if the specified URI is

null
**Throws:** IllegalArgumentException

- if the URI scheme is not

"mailto"
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.MAIL

action
**Throws:** IOException

- if the user default mail client is not
found or fails to be launched
**Throws:** SecurityException

- if a security manager exists and it
denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
**See Also:** URI

,

AWTPermission

- addAppEventListener

```java
public void addAppEventListener​(
SystemEventListener
listener)
```

Adds sub-types of

SystemEventListener

to listen for notifications
from the native system.

Has no effect if SystemEventListener's sub-type is unsupported on the current
platform.

**Parameters:** listener

- listener
**Throws:** SecurityException

- if a security manager exists and it
denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Since:** 9
**See Also:** AppForegroundListener

,

AppHiddenListener

,

AppReopenedListener

,

ScreenSleepListener

,

SystemSleepListener

,

UserSessionListener

- removeAppEventListener

```java
public void removeAppEventListener​(
SystemEventListener
listener)
```

Removes sub-types of

SystemEventListener

to listen for notifications
from the native system.

Has no effect if SystemEventListener's sub-type is unsupported on the current
platform.

**Parameters:** listener

- listener
**Throws:** SecurityException

- if a security manager exists and it
denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Since:** 9
**See Also:** AppForegroundListener

,

AppHiddenListener

,

AppReopenedListener

,

ScreenSleepListener

,

SystemSleepListener

,

UserSessionListener

- setAboutHandler

```java
public void setAboutHandler​(
AboutHandler
aboutHandler)
```

Installs a handler to show a custom About window for your application.

Setting the

AboutHandler

to

null

reverts it to the
default behavior.

**Parameters:** aboutHandler

- the handler to respond to the

AboutHandler.handleAbout(AboutEvent)

message
**Throws:** SecurityException

- if a security manager exists and it
denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_ABOUT

action
**Since:** 9

- setPreferencesHandler

```java
public void setPreferencesHandler​(
PreferencesHandler
preferencesHandler)
```

Installs a handler to show a custom Preferences window for your
application.

Setting the

PreferencesHandler

to

null

reverts it to
the default behavior

**Parameters:** preferencesHandler

- the handler to respond to the

PreferencesHandler.handlePreferences(PreferencesEvent)
**Throws:** SecurityException

- if a security manager exists and it
denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_PREFERENCES

action
**Since:** 9

- setOpenFileHandler

```java
public void setOpenFileHandler​(
OpenFilesHandler
openFileHandler)
```

Installs the handler which is notified when the application is asked to
open a list of files.

**Implementation Note:** Please note that for macOS, notifications
are only sent if the Java app is a bundled application,
with a

CFBundleDocumentTypes

array present in its

Info.plist

. Check the

Apple Developer Documentation

for more information about

Info.plist

.
**Parameters:** openFileHandler

- handler
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkRead(java.lang.String)

method denies read access to the files, or it denies the

RuntimePermission("canProcessApplicationEvents")

permission, or the calling thread is not allowed to create a
subprocess
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_OPEN_FILE

action
**Since:** 9

- setPrintFileHandler

```java
public void setPrintFileHandler​(
PrintFilesHandler
printFileHandler)
```

Installs the handler which is notified when the application is asked to
print a list of files.

**Implementation Note:** Please note that for macOS, notifications
are only sent if the Java app is a bundled application,
with a

CFBundleDocumentTypes

array present in its

Info.plist

. Check the

Apple Developer Documentation

for more information about

Info.plist

.
**Parameters:** printFileHandler

- handler
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkPrintJobAccess()

method denies
the permission to print or it denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_PRINT_FILE

action
**Since:** 9

- setOpenURIHandler

```java
public void setOpenURIHandler​(
OpenURIHandler
openURIHandler)
```

Installs the handler which is notified when the application is asked to
open a URL.

Setting the handler to

null

causes all

OpenURIHandler.openURI(OpenURIEvent)

requests to be
enqueued until another handler is set.

**Implementation Note:** Please note that for macOS, notifications
are only sent if the Java app is a bundled application,
with a

CFBundleDocumentTypes

array present in its

Info.plist

. Check the

Apple Developer Documentation

for more information about

Info.plist

.
**Parameters:** openURIHandler

- handler

RuntimePermission("canProcessApplicationEvents")

permission, or the calling thread is not allowed to create a
subprocess
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_OPEN_URI

action
**Since:** 9

- setQuitHandler

```java
public void setQuitHandler​(
QuitHandler
quitHandler)
```

Installs the handler which determines if the application should quit. The
handler is passed a one-shot

QuitResponse

which can cancel or
proceed with the quit. Setting the handler to

null

causes
all quit requests to directly perform the default

QuitStrategy

.

**Parameters:** quitHandler

- the handler that is called when the application is
asked to quit
**Throws:** SecurityException

- if a security manager exists and it
will not allow the caller to invoke

System.exit

or it denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_QUIT_HANDLER

action
**Since:** 9

- setQuitStrategy

```java
public void setQuitStrategy​(
QuitStrategy
strategy)
```

Sets the default strategy used to quit this application. The default is
calling SYSTEM_EXIT_0.

**Parameters:** strategy

- the way this application should be shutdown
**Throws:** SecurityException

- if a security manager exists and it
will not allow the caller to invoke

System.exit

or it denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_QUIT_STRATEGY

action
**Since:** 9
**See Also:** QuitStrategy

- enableSuddenTermination

```java
public void enableSuddenTermination()
```

Enables this application to be suddenly terminated.

Call this method to indicate your application's state is saved, and
requires no notification to be terminated. Letting your application
remain terminatable improves the user experience by avoiding re-paging in
your application when it's asked to quit.

Note: enabling sudden termination will allow your application to be
quit without notifying your QuitHandler, or running any shutdown
hooks.

E.g. user-initiated Cmd-Q, logout, restart, or shutdown requests will
effectively "kill -KILL" your application.

**Throws:** SecurityException

- if a security manager exists and it
will not allow the caller to invoke

System.exit

or it denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_SUDDEN_TERMINATION

action
**Since:** 9
**See Also:** disableSuddenTermination()

- disableSuddenTermination

```java
public void disableSuddenTermination()
```

Prevents this application from being suddenly terminated.

Call this method to indicate that your application has unsaved state, and
may not be terminated without notification.

**Throws:** SecurityException

- if a security manager exists and it
will not allow the caller to invoke

System.exit

or it denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_SUDDEN_TERMINATION

action
**Since:** 9
**See Also:** enableSuddenTermination()

- requestForeground

```java
public void requestForeground​(boolean allWindows)
```

Requests this application to move to the foreground.

**Parameters:** allWindows

- if all windows of this application should be moved to
the foreground, or only the foremost one
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_REQUEST_FOREGROUND

action
**Since:** 9

- openHelpViewer

```java
public void openHelpViewer()
```

Opens the native help viewer application.

**Implementation Note:** Please note that for Mac OS, it opens the native help viewer
application if a Help Book has been added to the application bundler
and registered in the Info.plist with CFBundleHelpBookFolder
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission, or it denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_HELP_VIEWER

action
**Since:** 9

- setDefaultMenuBar

```java
public void setDefaultMenuBar​(
JMenuBar
menuBar)
```

Sets the default menu bar to use when there are no active frames.

**Parameters:** menuBar

- to use when no other frames are active
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_MENU_BAR

action
**Since:** 9

- browseFileDirectory

```java
public void browseFileDirectory​(
File
file)
```

Opens a folder containing the

file

and selects it
in a default system file manager.

**Parameters:** file

- the file
**Throws:** SecurityException

- If a security manager exists and its

SecurityManager.checkRead(java.lang.String)

method
denies read access to the file or to its parent, or it denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.BROWSE_FILE_DIR

action
**Throws:** NullPointerException

- if

file

is

null
**Throws:** IllegalArgumentException

- if the specified file or its parent
doesn't exist
**Since:** 9

- moveToTrash

```java
public boolean moveToTrash​(
File
file)
```

Moves the specified file to the trash.

**Parameters:** file

- the file
**Returns:** returns true if successfully moved the file to the trash.
**Throws:** SecurityException

- If a security manager exists and its

SecurityManager.checkDelete(java.lang.String)

method
denies deletion of the file
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.MOVE_TO_TRASH

action
**Throws:** NullPointerException

- if

file

is

null
**Throws:** IllegalArgumentException

- if the specified file doesn't exist
**Since:** 9

---

#### Method Detail

getDesktop

```java
public static
Desktop
getDesktop()
```

Returns the

Desktop

instance of the current
desktop context. On some platforms the Desktop API may not be
supported; use the

isDesktopSupported()

method to
determine if the current desktop is supported.

**Returns:** the Desktop instance
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** UnsupportedOperationException

- if this class is not
supported on the current platform
**See Also:** isDesktopSupported()

,

GraphicsEnvironment.isHeadless()

---

#### getDesktop

public static

Desktop

getDesktop()

Returns the

Desktop

instance of the current
desktop context. On some platforms the Desktop API may not be
supported; use the

isDesktopSupported()

method to
determine if the current desktop is supported.

isDesktopSupported

```java
public static boolean isDesktopSupported()
```

Tests whether this class is supported on the current platform.
If it's supported, use

getDesktop()

to retrieve an
instance.

**Returns:** true

if this class is supported on the
current platform;

false

otherwise
**See Also:** getDesktop()

---

#### isDesktopSupported

public static boolean isDesktopSupported()

Tests whether this class is supported on the current platform.
If it's supported, use

getDesktop()

to retrieve an
instance.

isSupported

```java
public boolean isSupported​(
Desktop.Action
action)
```

Tests whether an action is supported on the current platform.

Even when the platform supports an action, a file or URI may
not have a registered application for the action. For example,
most of the platforms support the

Desktop.Action.OPEN

action. But for a specific file, there may not be an
application registered to open it. In this case,

isSupported(Action)

may return

true

, but the corresponding
action method will throw an

IOException

.

**Parameters:** action

- the specified

Desktop.Action
**Returns:** true

if the specified action is supported on
the current platform;

false

otherwise
**See Also:** Desktop.Action

---

#### isSupported

public boolean isSupported​(

Desktop.Action

action)

Tests whether an action is supported on the current platform.

Even when the platform supports an action, a file or URI may
not have a registered application for the action. For example,
most of the platforms support the

Desktop.Action.OPEN

action. But for a specific file, there may not be an
application registered to open it. In this case,

isSupported(Action)

may return

true

, but the corresponding
action method will throw an

IOException

.

Even when the platform supports an action, a file or URI may
not have a registered application for the action. For example,
most of the platforms support the

Desktop.Action.OPEN

action. But for a specific file, there may not be an
application registered to open it. In this case,

isSupported(Action)

may return

true

, but the corresponding
action method will throw an

IOException

.

open

```java
public void open​(
File
file)
throws
IOException
```

Launches the associated application to open the file.

If the specified file is a directory, the file manager of
the current platform is launched to open it.

**Parameters:** file

- the file to be opened with the associated application
**Throws:** NullPointerException

- if

file

is

null
**Throws:** IllegalArgumentException

- if the specified file doesn't
exist
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.OPEN

action
**Throws:** IOException

- if the specified file has no associated
application or the associated application fails to be launched
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkRead(java.lang.String)

method denies read access to the file, or it denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
**See Also:** AWTPermission

---

#### open

public void open​(

File

file)
throws

IOException

Launches the associated application to open the file.

If the specified file is a directory, the file manager of
the current platform is launched to open it.

If the specified file is a directory, the file manager of
the current platform is launched to open it.

edit

```java
public void edit​(
File
file)
throws
IOException
```

Launches the associated editor application and opens a file for
editing.

**Parameters:** file

- the file to be opened for editing
**Throws:** NullPointerException

- if the specified file is

null
**Throws:** IllegalArgumentException

- if the specified file doesn't
exist
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.EDIT

action
**Throws:** IOException

- if the specified file has no associated
editor, or the associated application fails to be launched
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkRead(java.lang.String)

method denies read access to the file, or

SecurityManager.checkWrite(java.lang.String)

method
denies write access to the file, or it denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
**See Also:** AWTPermission

---

#### edit

public void edit​(

File

file)
throws

IOException

Launches the associated editor application and opens a file for
editing.

print

```java
public void print​(
File
file)
throws
IOException
```

Prints a file with the native desktop printing facility, using
the associated application's print command.

**Parameters:** file

- the file to be printed
**Throws:** NullPointerException

- if the specified file is

null
**Throws:** IllegalArgumentException

- if the specified file doesn't
exist
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.PRINT

action
**Throws:** IOException

- if the specified file has no associated
application that can be used to print it
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkRead(java.lang.String)

method denies read access to the file, or its

SecurityManager.checkPrintJobAccess()

method denies
the permission to print the file, or the calling thread is not
allowed to create a subprocess

---

#### print

public void print​(

File

file)
throws

IOException

Prints a file with the native desktop printing facility, using
the associated application's print command.

browse

```java
public void browse​(
URI
uri)
throws
IOException
```

Launches the default browser to display a

URI

.
If the default browser is not able to handle the specified

URI

, the application registered for handling

URIs

of the specified type is invoked. The application
is determined from the protocol and path of the

URI

, as
defined by the

URI

class.

**Parameters:** uri

- the URI to be displayed in the user default browser
**Throws:** NullPointerException

- if

uri

is

null
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.BROWSE

action
**Throws:** IOException

- if the user default browser is not found,
or it fails to be launched, or the default handler application
failed to be launched
**Throws:** SecurityException

- if a security manager exists and it
denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
**See Also:** URI

,

AWTPermission

---

#### browse

public void browse​(

URI

uri)
throws

IOException

Launches the default browser to display a

URI

.
If the default browser is not able to handle the specified

URI

, the application registered for handling

URIs

of the specified type is invoked. The application
is determined from the protocol and path of the

URI

, as
defined by the

URI

class.

mail

```java
public void mail()
throws
IOException
```

Launches the mail composing window of the user default mail
client.

**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.MAIL

action
**Throws:** IOException

- if the user default mail client is not
found, or it fails to be launched
**Throws:** SecurityException

- if a security manager exists and it
denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
**See Also:** AWTPermission

---

#### mail

public void mail()
throws

IOException

Launches the mail composing window of the user default mail
client.

mail

```java
public void mail​(
URI
mailtoURI)
throws
IOException
```

Launches the mail composing window of the user default mail
client, filling the message fields specified by a

mailto:

URI.

A

mailto:

URI can specify message fields
including

"to"

,

"cc"

,

"subject"

,

"body"

, etc. See

The mailto URL
scheme (RFC 2368)

for the

mailto:

URI specification
details.

**Parameters:** mailtoURI

- the specified

mailto:

URI
**Throws:** NullPointerException

- if the specified URI is

null
**Throws:** IllegalArgumentException

- if the URI scheme is not

"mailto"
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.MAIL

action
**Throws:** IOException

- if the user default mail client is not
found or fails to be launched
**Throws:** SecurityException

- if a security manager exists and it
denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
**See Also:** URI

,

AWTPermission

---

#### mail

public void mail​(

URI

mailtoURI)
throws

IOException

Launches the mail composing window of the user default mail
client, filling the message fields specified by a

mailto:

URI.

A

mailto:

URI can specify message fields
including

"to"

,

"cc"

,

"subject"

,

"body"

, etc. See

The mailto URL
scheme (RFC 2368)

for the

mailto:

URI specification
details.

A

mailto:

URI can specify message fields
including

"to"

,

"cc"

,

"subject"

,

"body"

, etc. See

The mailto URL
scheme (RFC 2368)

for the

mailto:

URI specification
details.

addAppEventListener

```java
public void addAppEventListener​(
SystemEventListener
listener)
```

Adds sub-types of

SystemEventListener

to listen for notifications
from the native system.

Has no effect if SystemEventListener's sub-type is unsupported on the current
platform.

**Parameters:** listener

- listener
**Throws:** SecurityException

- if a security manager exists and it
denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Since:** 9
**See Also:** AppForegroundListener

,

AppHiddenListener

,

AppReopenedListener

,

ScreenSleepListener

,

SystemSleepListener

,

UserSessionListener

---

#### addAppEventListener

public void addAppEventListener​(

SystemEventListener

listener)

Adds sub-types of

SystemEventListener

to listen for notifications
from the native system.

Has no effect if SystemEventListener's sub-type is unsupported on the current
platform.

removeAppEventListener

```java
public void removeAppEventListener​(
SystemEventListener
listener)
```

Removes sub-types of

SystemEventListener

to listen for notifications
from the native system.

Has no effect if SystemEventListener's sub-type is unsupported on the current
platform.

**Parameters:** listener

- listener
**Throws:** SecurityException

- if a security manager exists and it
denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Since:** 9
**See Also:** AppForegroundListener

,

AppHiddenListener

,

AppReopenedListener

,

ScreenSleepListener

,

SystemSleepListener

,

UserSessionListener

---

#### removeAppEventListener

public void removeAppEventListener​(

SystemEventListener

listener)

Removes sub-types of

SystemEventListener

to listen for notifications
from the native system.

Has no effect if SystemEventListener's sub-type is unsupported on the current
platform.

setAboutHandler

```java
public void setAboutHandler​(
AboutHandler
aboutHandler)
```

Installs a handler to show a custom About window for your application.

Setting the

AboutHandler

to

null

reverts it to the
default behavior.

**Parameters:** aboutHandler

- the handler to respond to the

AboutHandler.handleAbout(AboutEvent)

message
**Throws:** SecurityException

- if a security manager exists and it
denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_ABOUT

action
**Since:** 9

---

#### setAboutHandler

public void setAboutHandler​(

AboutHandler

aboutHandler)

Installs a handler to show a custom About window for your application.

Setting the

AboutHandler

to

null

reverts it to the
default behavior.

Setting the

AboutHandler

to

null

reverts it to the
default behavior.

setPreferencesHandler

```java
public void setPreferencesHandler​(
PreferencesHandler
preferencesHandler)
```

Installs a handler to show a custom Preferences window for your
application.

Setting the

PreferencesHandler

to

null

reverts it to
the default behavior

**Parameters:** preferencesHandler

- the handler to respond to the

PreferencesHandler.handlePreferences(PreferencesEvent)
**Throws:** SecurityException

- if a security manager exists and it
denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_PREFERENCES

action
**Since:** 9

---

#### setPreferencesHandler

public void setPreferencesHandler​(

PreferencesHandler

preferencesHandler)

Installs a handler to show a custom Preferences window for your
application.

Setting the

PreferencesHandler

to

null

reverts it to
the default behavior

Setting the

PreferencesHandler

to

null

reverts it to
the default behavior

setOpenFileHandler

```java
public void setOpenFileHandler​(
OpenFilesHandler
openFileHandler)
```

Installs the handler which is notified when the application is asked to
open a list of files.

**Implementation Note:** Please note that for macOS, notifications
are only sent if the Java app is a bundled application,
with a

CFBundleDocumentTypes

array present in its

Info.plist

. Check the

Apple Developer Documentation

for more information about

Info.plist

.
**Parameters:** openFileHandler

- handler
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkRead(java.lang.String)

method denies read access to the files, or it denies the

RuntimePermission("canProcessApplicationEvents")

permission, or the calling thread is not allowed to create a
subprocess
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_OPEN_FILE

action
**Since:** 9

---

#### setOpenFileHandler

public void setOpenFileHandler​(

OpenFilesHandler

openFileHandler)

Installs the handler which is notified when the application is asked to
open a list of files.

setPrintFileHandler

```java
public void setPrintFileHandler​(
PrintFilesHandler
printFileHandler)
```

Installs the handler which is notified when the application is asked to
print a list of files.

**Implementation Note:** Please note that for macOS, notifications
are only sent if the Java app is a bundled application,
with a

CFBundleDocumentTypes

array present in its

Info.plist

. Check the

Apple Developer Documentation

for more information about

Info.plist

.
**Parameters:** printFileHandler

- handler
**Throws:** SecurityException

- if a security manager exists and its

SecurityManager.checkPrintJobAccess()

method denies
the permission to print or it denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_PRINT_FILE

action
**Since:** 9

---

#### setPrintFileHandler

public void setPrintFileHandler​(

PrintFilesHandler

printFileHandler)

Installs the handler which is notified when the application is asked to
print a list of files.

setOpenURIHandler

```java
public void setOpenURIHandler​(
OpenURIHandler
openURIHandler)
```

Installs the handler which is notified when the application is asked to
open a URL.

Setting the handler to

null

causes all

OpenURIHandler.openURI(OpenURIEvent)

requests to be
enqueued until another handler is set.

**Implementation Note:** Please note that for macOS, notifications
are only sent if the Java app is a bundled application,
with a

CFBundleDocumentTypes

array present in its

Info.plist

. Check the

Apple Developer Documentation

for more information about

Info.plist

.
**Parameters:** openURIHandler

- handler

RuntimePermission("canProcessApplicationEvents")

permission, or the calling thread is not allowed to create a
subprocess
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_OPEN_URI

action
**Since:** 9

---

#### setOpenURIHandler

public void setOpenURIHandler​(

OpenURIHandler

openURIHandler)

Installs the handler which is notified when the application is asked to
open a URL.

Setting the handler to

null

causes all

OpenURIHandler.openURI(OpenURIEvent)

requests to be
enqueued until another handler is set.

setQuitHandler

```java
public void setQuitHandler​(
QuitHandler
quitHandler)
```

Installs the handler which determines if the application should quit. The
handler is passed a one-shot

QuitResponse

which can cancel or
proceed with the quit. Setting the handler to

null

causes
all quit requests to directly perform the default

QuitStrategy

.

**Parameters:** quitHandler

- the handler that is called when the application is
asked to quit
**Throws:** SecurityException

- if a security manager exists and it
will not allow the caller to invoke

System.exit

or it denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_QUIT_HANDLER

action
**Since:** 9

---

#### setQuitHandler

public void setQuitHandler​(

QuitHandler

quitHandler)

Installs the handler which determines if the application should quit. The
handler is passed a one-shot

QuitResponse

which can cancel or
proceed with the quit. Setting the handler to

null

causes
all quit requests to directly perform the default

QuitStrategy

.

setQuitStrategy

```java
public void setQuitStrategy​(
QuitStrategy
strategy)
```

Sets the default strategy used to quit this application. The default is
calling SYSTEM_EXIT_0.

**Parameters:** strategy

- the way this application should be shutdown
**Throws:** SecurityException

- if a security manager exists and it
will not allow the caller to invoke

System.exit

or it denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_QUIT_STRATEGY

action
**Since:** 9
**See Also:** QuitStrategy

---

#### setQuitStrategy

public void setQuitStrategy​(

QuitStrategy

strategy)

Sets the default strategy used to quit this application. The default is
calling SYSTEM_EXIT_0.

enableSuddenTermination

```java
public void enableSuddenTermination()
```

Enables this application to be suddenly terminated.

Call this method to indicate your application's state is saved, and
requires no notification to be terminated. Letting your application
remain terminatable improves the user experience by avoiding re-paging in
your application when it's asked to quit.

Note: enabling sudden termination will allow your application to be
quit without notifying your QuitHandler, or running any shutdown
hooks.

E.g. user-initiated Cmd-Q, logout, restart, or shutdown requests will
effectively "kill -KILL" your application.

**Throws:** SecurityException

- if a security manager exists and it
will not allow the caller to invoke

System.exit

or it denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_SUDDEN_TERMINATION

action
**Since:** 9
**See Also:** disableSuddenTermination()

---

#### enableSuddenTermination

public void enableSuddenTermination()

Enables this application to be suddenly terminated.

Call this method to indicate your application's state is saved, and
requires no notification to be terminated. Letting your application
remain terminatable improves the user experience by avoiding re-paging in
your application when it's asked to quit.

Note: enabling sudden termination will allow your application to be
quit without notifying your QuitHandler, or running any shutdown
hooks.

E.g. user-initiated Cmd-Q, logout, restart, or shutdown requests will
effectively "kill -KILL" your application.

disableSuddenTermination

```java
public void disableSuddenTermination()
```

Prevents this application from being suddenly terminated.

Call this method to indicate that your application has unsaved state, and
may not be terminated without notification.

**Throws:** SecurityException

- if a security manager exists and it
will not allow the caller to invoke

System.exit

or it denies the

RuntimePermission("canProcessApplicationEvents")

permission
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_SUDDEN_TERMINATION

action
**Since:** 9
**See Also:** enableSuddenTermination()

---

#### disableSuddenTermination

public void disableSuddenTermination()

Prevents this application from being suddenly terminated.

Call this method to indicate that your application has unsaved state, and
may not be terminated without notification.

requestForeground

```java
public void requestForeground​(boolean allWindows)
```

Requests this application to move to the foreground.

**Parameters:** allWindows

- if all windows of this application should be moved to
the foreground, or only the foremost one
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_REQUEST_FOREGROUND

action
**Since:** 9

---

#### requestForeground

public void requestForeground​(boolean allWindows)

Requests this application to move to the foreground.

openHelpViewer

```java
public void openHelpViewer()
```

Opens the native help viewer application.

**Implementation Note:** Please note that for Mac OS, it opens the native help viewer
application if a Help Book has been added to the application bundler
and registered in the Info.plist with CFBundleHelpBookFolder
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission, or it denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_HELP_VIEWER

action
**Since:** 9

---

#### openHelpViewer

public void openHelpViewer()

Opens the native help viewer application.

setDefaultMenuBar

```java
public void setDefaultMenuBar​(
JMenuBar
menuBar)
```

Sets the default menu bar to use when there are no active frames.

**Parameters:** menuBar

- to use when no other frames are active
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.APP_MENU_BAR

action
**Since:** 9

---

#### setDefaultMenuBar

public void setDefaultMenuBar​(

JMenuBar

menuBar)

Sets the default menu bar to use when there are no active frames.

browseFileDirectory

```java
public void browseFileDirectory​(
File
file)
```

Opens a folder containing the

file

and selects it
in a default system file manager.

**Parameters:** file

- the file
**Throws:** SecurityException

- If a security manager exists and its

SecurityManager.checkRead(java.lang.String)

method
denies read access to the file or to its parent, or it denies the

AWTPermission("showWindowWithoutWarningBanner")

permission, or the calling thread is not allowed to create a
subprocess
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.BROWSE_FILE_DIR

action
**Throws:** NullPointerException

- if

file

is

null
**Throws:** IllegalArgumentException

- if the specified file or its parent
doesn't exist
**Since:** 9

---

#### browseFileDirectory

public void browseFileDirectory​(

File

file)

Opens a folder containing the

file

and selects it
in a default system file manager.

moveToTrash

```java
public boolean moveToTrash​(
File
file)
```

Moves the specified file to the trash.

**Parameters:** file

- the file
**Returns:** returns true if successfully moved the file to the trash.
**Throws:** SecurityException

- If a security manager exists and its

SecurityManager.checkDelete(java.lang.String)

method
denies deletion of the file
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Desktop.Action.MOVE_TO_TRASH

action
**Throws:** NullPointerException

- if

file

is

null
**Throws:** IllegalArgumentException

- if the specified file doesn't exist
**Since:** 9

---

#### moveToTrash

public boolean moveToTrash​(

File

file)

Moves the specified file to the trash.

---

