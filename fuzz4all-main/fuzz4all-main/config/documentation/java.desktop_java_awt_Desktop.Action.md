# Enum Desktop.Action

**Source:** `java.desktop\java\awt\Desktop.Action.html`

### Class Description

```java
public static enum
Desktop.Action

extends
Enum
<
Desktop.Action
>
```

Represents an action type. Each platform supports a different
set of actions. You may use the

Desktop.isSupported(java.awt.Desktop.Action)

method to determine if the given action is supported by the
current platform.

**All Implemented Interfaces:** Serializable

,

Comparable

<

Desktop.Action

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Desktop.Action
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Desktop.Action c : Desktop.Action.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
Desktop.Action
valueOf​(
String
name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:**
- name

- the name of the enum constant to be returned.

**Returns:**
- the enum constant with the specified name

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with the specified name
- NullPointerException

- if the argument is null

---

### Additional Sections

#### Enum Desktop.Action

java.lang.Object

- java.lang.Enum

<

Desktop.Action

>
- - java.awt.Desktop.Action

java.lang.Enum

<

Desktop.Action

>

- java.awt.Desktop.Action

java.awt.Desktop.Action

**All Implemented Interfaces:** Serializable

,

Comparable

<

Desktop.Action

>

**Enclosing class:** Desktop

```java
public static enum
Desktop.Action

extends
Enum
<
Desktop.Action
>
```

Represents an action type. Each platform supports a different
set of actions. You may use the

Desktop.isSupported(java.awt.Desktop.Action)

method to determine if the given action is supported by the
current platform.

**Since:** 1.6
**See Also:** Desktop.isSupported(java.awt.Desktop.Action)

public static enum

Desktop.Action

extends

Enum

<

Desktop.Action

>

Represents an action type. Each platform supports a different
set of actions. You may use the

Desktop.isSupported(java.awt.Desktop.Action)

method to determine if the given action is supported by the
current platform.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

APP_ABOUT

Represents an AboutHandler

APP_EVENT_FOREGROUND

Represents an AppForegroundListener

APP_EVENT_HIDDEN

Represents an AppHiddenListener

APP_EVENT_REOPENED

Represents an AppReopenedListener

APP_EVENT_SCREEN_SLEEP

Represents a ScreenSleepListener

APP_EVENT_SYSTEM_SLEEP

Represents a SystemSleepListener

APP_EVENT_USER_SESSION

Represents a UserSessionListener

APP_HELP_VIEWER

Represents a HelpViewer

APP_MENU_BAR

Represents a menu bar

APP_OPEN_FILE

Represents an OpenFilesHandler

APP_OPEN_URI

Represents an OpenURIHandler

APP_PREFERENCES

Represents a PreferencesHandler

APP_PRINT_FILE

Represents a PrintFilesHandler

APP_QUIT_HANDLER

Represents a QuitHandler

APP_QUIT_STRATEGY

Represents a QuitStrategy

APP_REQUEST_FOREGROUND

Represents a requestForeground

APP_SUDDEN_TERMINATION

Represents a SuddenTermination

BROWSE

Represents a "browse" action.

BROWSE_FILE_DIR

Represents a browse file directory

EDIT

Represents an "edit" action.

MAIL

Represents a "mail" action.

MOVE_TO_TRASH

Represents a move to trash

OPEN

Represents an "open" action.

PRINT

Represents a "print" action.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Desktop.Action

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Desktop.Action

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Enum Constant Summary

Enum Constants

Enum Constant

Description

APP_ABOUT

Represents an AboutHandler

APP_EVENT_FOREGROUND

Represents an AppForegroundListener

APP_EVENT_HIDDEN

Represents an AppHiddenListener

APP_EVENT_REOPENED

Represents an AppReopenedListener

APP_EVENT_SCREEN_SLEEP

Represents a ScreenSleepListener

APP_EVENT_SYSTEM_SLEEP

Represents a SystemSleepListener

APP_EVENT_USER_SESSION

Represents a UserSessionListener

APP_HELP_VIEWER

Represents a HelpViewer

APP_MENU_BAR

Represents a menu bar

APP_OPEN_FILE

Represents an OpenFilesHandler

APP_OPEN_URI

Represents an OpenURIHandler

APP_PREFERENCES

Represents a PreferencesHandler

APP_PRINT_FILE

Represents a PrintFilesHandler

APP_QUIT_HANDLER

Represents a QuitHandler

APP_QUIT_STRATEGY

Represents a QuitStrategy

APP_REQUEST_FOREGROUND

Represents a requestForeground

APP_SUDDEN_TERMINATION

Represents a SuddenTermination

BROWSE

Represents a "browse" action.

BROWSE_FILE_DIR

Represents a browse file directory

EDIT

Represents an "edit" action.

MAIL

Represents a "mail" action.

MOVE_TO_TRASH

Represents a move to trash

OPEN

Represents an "open" action.

PRINT

Represents a "print" action.

---

#### Enum Constant Summary

Represents an AboutHandler

Represents an AppForegroundListener

Represents an AppHiddenListener

Represents an AppReopenedListener

Represents a ScreenSleepListener

Represents a SystemSleepListener

Represents a UserSessionListener

Represents a HelpViewer

Represents a menu bar

Represents an OpenFilesHandler

Represents an OpenURIHandler

Represents a PreferencesHandler

Represents a PrintFilesHandler

Represents a QuitHandler

Represents a QuitStrategy

Represents a requestForeground

Represents a SuddenTermination

Represents a "browse" action.

Represents a browse file directory

Represents an "edit" action.

Represents a "mail" action.

Represents a move to trash

Represents an "open" action.

Represents a "print" action.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Desktop.Action

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

Desktop.Action

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the enum constant of this type with the specified name.

Returns an array containing the constants of this enum type, in
the order they are declared.

Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

---

#### Methods declared in class java.lang. Enum

Methods declared in class java.lang.

Object

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- OPEN

```java
public static final
Desktop.Action
OPEN
```

Represents an "open" action.

**See Also:** Desktop.open(java.io.File)

- EDIT

```java
public static final
Desktop.Action
EDIT
```

Represents an "edit" action.

**See Also:** Desktop.edit(java.io.File)

- PRINT

```java
public static final
Desktop.Action
PRINT
```

Represents a "print" action.

**See Also:** Desktop.print(java.io.File)

- MAIL

```java
public static final
Desktop.Action
MAIL
```

Represents a "mail" action.

**See Also:** Desktop.mail()

,

Desktop.mail(java.net.URI)

- BROWSE

```java
public static final
Desktop.Action
BROWSE
```

Represents a "browse" action.

**See Also:** Desktop.browse(java.net.URI)

- APP_EVENT_FOREGROUND

```java
public static final
Desktop.Action
APP_EVENT_FOREGROUND
```

Represents an AppForegroundListener

**Since:** 9
**See Also:** AppForegroundListener

- APP_EVENT_HIDDEN

```java
public static final
Desktop.Action
APP_EVENT_HIDDEN
```

Represents an AppHiddenListener

**Since:** 9
**See Also:** AppHiddenListener

- APP_EVENT_REOPENED

```java
public static final
Desktop.Action
APP_EVENT_REOPENED
```

Represents an AppReopenedListener

**Since:** 9
**See Also:** AppReopenedListener

- APP_EVENT_SCREEN_SLEEP

```java
public static final
Desktop.Action
APP_EVENT_SCREEN_SLEEP
```

Represents a ScreenSleepListener

**Since:** 9
**See Also:** ScreenSleepListener

- APP_EVENT_SYSTEM_SLEEP

```java
public static final
Desktop.Action
APP_EVENT_SYSTEM_SLEEP
```

Represents a SystemSleepListener

**Since:** 9
**See Also:** SystemSleepListener

- APP_EVENT_USER_SESSION

```java
public static final
Desktop.Action
APP_EVENT_USER_SESSION
```

Represents a UserSessionListener

**Since:** 9
**See Also:** UserSessionListener

- APP_ABOUT

```java
public static final
Desktop.Action
APP_ABOUT
```

Represents an AboutHandler

**Since:** 9
**See Also:** Desktop.setAboutHandler(java.awt.desktop.AboutHandler)

- APP_PREFERENCES

```java
public static final
Desktop.Action
APP_PREFERENCES
```

Represents a PreferencesHandler

**Since:** 9
**See Also:** Desktop.setPreferencesHandler(java.awt.desktop.PreferencesHandler)

- APP_OPEN_FILE

```java
public static final
Desktop.Action
APP_OPEN_FILE
```

Represents an OpenFilesHandler

**Since:** 9
**See Also:** Desktop.setOpenFileHandler(java.awt.desktop.OpenFilesHandler)

- APP_PRINT_FILE

```java
public static final
Desktop.Action
APP_PRINT_FILE
```

Represents a PrintFilesHandler

**Since:** 9
**See Also:** Desktop.setPrintFileHandler(java.awt.desktop.PrintFilesHandler)

- APP_OPEN_URI

```java
public static final
Desktop.Action
APP_OPEN_URI
```

Represents an OpenURIHandler

**Since:** 9
**See Also:** Desktop.setOpenURIHandler(java.awt.desktop.OpenURIHandler)

- APP_QUIT_HANDLER

```java
public static final
Desktop.Action
APP_QUIT_HANDLER
```

Represents a QuitHandler

**Since:** 9
**See Also:** Desktop.setQuitHandler(java.awt.desktop.QuitHandler)

- APP_QUIT_STRATEGY

```java
public static final
Desktop.Action
APP_QUIT_STRATEGY
```

Represents a QuitStrategy

**Since:** 9
**See Also:** Desktop.setQuitStrategy(java.awt.desktop.QuitStrategy)

- APP_SUDDEN_TERMINATION

```java
public static final
Desktop.Action
APP_SUDDEN_TERMINATION
```

Represents a SuddenTermination

**Since:** 9
**See Also:** Desktop.enableSuddenTermination()

- APP_REQUEST_FOREGROUND

```java
public static final
Desktop.Action
APP_REQUEST_FOREGROUND
```

Represents a requestForeground

**Since:** 9
**See Also:** Desktop.requestForeground(boolean)

- APP_HELP_VIEWER

```java
public static final
Desktop.Action
APP_HELP_VIEWER
```

Represents a HelpViewer

**Since:** 9
**See Also:** Desktop.openHelpViewer()

- APP_MENU_BAR

```java
public static final
Desktop.Action
APP_MENU_BAR
```

Represents a menu bar

**Since:** 9
**See Also:** Desktop.setDefaultMenuBar(javax.swing.JMenuBar)

- BROWSE_FILE_DIR

```java
public static final
Desktop.Action
BROWSE_FILE_DIR
```

Represents a browse file directory

**Since:** 9
**See Also:** Desktop.browseFileDirectory(java.io.File)

- MOVE_TO_TRASH

```java
public static final
Desktop.Action
MOVE_TO_TRASH
```

Represents a move to trash

**Since:** 9
**See Also:** Desktop.moveToTrash(java.io.File)

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
Desktop.Action
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Desktop.Action c : Desktop.Action.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Desktop.Action
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

Enum Constant Detail

- OPEN

```java
public static final
Desktop.Action
OPEN
```

Represents an "open" action.

**See Also:** Desktop.open(java.io.File)

- EDIT

```java
public static final
Desktop.Action
EDIT
```

Represents an "edit" action.

**See Also:** Desktop.edit(java.io.File)

- PRINT

```java
public static final
Desktop.Action
PRINT
```

Represents a "print" action.

**See Also:** Desktop.print(java.io.File)

- MAIL

```java
public static final
Desktop.Action
MAIL
```

Represents a "mail" action.

**See Also:** Desktop.mail()

,

Desktop.mail(java.net.URI)

- BROWSE

```java
public static final
Desktop.Action
BROWSE
```

Represents a "browse" action.

**See Also:** Desktop.browse(java.net.URI)

- APP_EVENT_FOREGROUND

```java
public static final
Desktop.Action
APP_EVENT_FOREGROUND
```

Represents an AppForegroundListener

**Since:** 9
**See Also:** AppForegroundListener

- APP_EVENT_HIDDEN

```java
public static final
Desktop.Action
APP_EVENT_HIDDEN
```

Represents an AppHiddenListener

**Since:** 9
**See Also:** AppHiddenListener

- APP_EVENT_REOPENED

```java
public static final
Desktop.Action
APP_EVENT_REOPENED
```

Represents an AppReopenedListener

**Since:** 9
**See Also:** AppReopenedListener

- APP_EVENT_SCREEN_SLEEP

```java
public static final
Desktop.Action
APP_EVENT_SCREEN_SLEEP
```

Represents a ScreenSleepListener

**Since:** 9
**See Also:** ScreenSleepListener

- APP_EVENT_SYSTEM_SLEEP

```java
public static final
Desktop.Action
APP_EVENT_SYSTEM_SLEEP
```

Represents a SystemSleepListener

**Since:** 9
**See Also:** SystemSleepListener

- APP_EVENT_USER_SESSION

```java
public static final
Desktop.Action
APP_EVENT_USER_SESSION
```

Represents a UserSessionListener

**Since:** 9
**See Also:** UserSessionListener

- APP_ABOUT

```java
public static final
Desktop.Action
APP_ABOUT
```

Represents an AboutHandler

**Since:** 9
**See Also:** Desktop.setAboutHandler(java.awt.desktop.AboutHandler)

- APP_PREFERENCES

```java
public static final
Desktop.Action
APP_PREFERENCES
```

Represents a PreferencesHandler

**Since:** 9
**See Also:** Desktop.setPreferencesHandler(java.awt.desktop.PreferencesHandler)

- APP_OPEN_FILE

```java
public static final
Desktop.Action
APP_OPEN_FILE
```

Represents an OpenFilesHandler

**Since:** 9
**See Also:** Desktop.setOpenFileHandler(java.awt.desktop.OpenFilesHandler)

- APP_PRINT_FILE

```java
public static final
Desktop.Action
APP_PRINT_FILE
```

Represents a PrintFilesHandler

**Since:** 9
**See Also:** Desktop.setPrintFileHandler(java.awt.desktop.PrintFilesHandler)

- APP_OPEN_URI

```java
public static final
Desktop.Action
APP_OPEN_URI
```

Represents an OpenURIHandler

**Since:** 9
**See Also:** Desktop.setOpenURIHandler(java.awt.desktop.OpenURIHandler)

- APP_QUIT_HANDLER

```java
public static final
Desktop.Action
APP_QUIT_HANDLER
```

Represents a QuitHandler

**Since:** 9
**See Also:** Desktop.setQuitHandler(java.awt.desktop.QuitHandler)

- APP_QUIT_STRATEGY

```java
public static final
Desktop.Action
APP_QUIT_STRATEGY
```

Represents a QuitStrategy

**Since:** 9
**See Also:** Desktop.setQuitStrategy(java.awt.desktop.QuitStrategy)

- APP_SUDDEN_TERMINATION

```java
public static final
Desktop.Action
APP_SUDDEN_TERMINATION
```

Represents a SuddenTermination

**Since:** 9
**See Also:** Desktop.enableSuddenTermination()

- APP_REQUEST_FOREGROUND

```java
public static final
Desktop.Action
APP_REQUEST_FOREGROUND
```

Represents a requestForeground

**Since:** 9
**See Also:** Desktop.requestForeground(boolean)

- APP_HELP_VIEWER

```java
public static final
Desktop.Action
APP_HELP_VIEWER
```

Represents a HelpViewer

**Since:** 9
**See Also:** Desktop.openHelpViewer()

- APP_MENU_BAR

```java
public static final
Desktop.Action
APP_MENU_BAR
```

Represents a menu bar

**Since:** 9
**See Also:** Desktop.setDefaultMenuBar(javax.swing.JMenuBar)

- BROWSE_FILE_DIR

```java
public static final
Desktop.Action
BROWSE_FILE_DIR
```

Represents a browse file directory

**Since:** 9
**See Also:** Desktop.browseFileDirectory(java.io.File)

- MOVE_TO_TRASH

```java
public static final
Desktop.Action
MOVE_TO_TRASH
```

Represents a move to trash

**Since:** 9
**See Also:** Desktop.moveToTrash(java.io.File)

---

#### Enum Constant Detail

OPEN

```java
public static final
Desktop.Action
OPEN
```

Represents an "open" action.

**See Also:** Desktop.open(java.io.File)

---

#### OPEN

public static final

Desktop.Action

OPEN

Represents an "open" action.

EDIT

```java
public static final
Desktop.Action
EDIT
```

Represents an "edit" action.

**See Also:** Desktop.edit(java.io.File)

---

#### EDIT

public static final

Desktop.Action

EDIT

Represents an "edit" action.

PRINT

```java
public static final
Desktop.Action
PRINT
```

Represents a "print" action.

**See Also:** Desktop.print(java.io.File)

---

#### PRINT

public static final

Desktop.Action

PRINT

Represents a "print" action.

MAIL

```java
public static final
Desktop.Action
MAIL
```

Represents a "mail" action.

**See Also:** Desktop.mail()

,

Desktop.mail(java.net.URI)

---

#### MAIL

public static final

Desktop.Action

MAIL

Represents a "mail" action.

BROWSE

```java
public static final
Desktop.Action
BROWSE
```

Represents a "browse" action.

**See Also:** Desktop.browse(java.net.URI)

---

#### BROWSE

public static final

Desktop.Action

BROWSE

Represents a "browse" action.

APP_EVENT_FOREGROUND

```java
public static final
Desktop.Action
APP_EVENT_FOREGROUND
```

Represents an AppForegroundListener

**Since:** 9
**See Also:** AppForegroundListener

---

#### APP_EVENT_FOREGROUND

public static final

Desktop.Action

APP_EVENT_FOREGROUND

Represents an AppForegroundListener

APP_EVENT_HIDDEN

```java
public static final
Desktop.Action
APP_EVENT_HIDDEN
```

Represents an AppHiddenListener

**Since:** 9
**See Also:** AppHiddenListener

---

#### APP_EVENT_HIDDEN

public static final

Desktop.Action

APP_EVENT_HIDDEN

Represents an AppHiddenListener

APP_EVENT_REOPENED

```java
public static final
Desktop.Action
APP_EVENT_REOPENED
```

Represents an AppReopenedListener

**Since:** 9
**See Also:** AppReopenedListener

---

#### APP_EVENT_REOPENED

public static final

Desktop.Action

APP_EVENT_REOPENED

Represents an AppReopenedListener

APP_EVENT_SCREEN_SLEEP

```java
public static final
Desktop.Action
APP_EVENT_SCREEN_SLEEP
```

Represents a ScreenSleepListener

**Since:** 9
**See Also:** ScreenSleepListener

---

#### APP_EVENT_SCREEN_SLEEP

public static final

Desktop.Action

APP_EVENT_SCREEN_SLEEP

Represents a ScreenSleepListener

APP_EVENT_SYSTEM_SLEEP

```java
public static final
Desktop.Action
APP_EVENT_SYSTEM_SLEEP
```

Represents a SystemSleepListener

**Since:** 9
**See Also:** SystemSleepListener

---

#### APP_EVENT_SYSTEM_SLEEP

public static final

Desktop.Action

APP_EVENT_SYSTEM_SLEEP

Represents a SystemSleepListener

APP_EVENT_USER_SESSION

```java
public static final
Desktop.Action
APP_EVENT_USER_SESSION
```

Represents a UserSessionListener

**Since:** 9
**See Also:** UserSessionListener

---

#### APP_EVENT_USER_SESSION

public static final

Desktop.Action

APP_EVENT_USER_SESSION

Represents a UserSessionListener

APP_ABOUT

```java
public static final
Desktop.Action
APP_ABOUT
```

Represents an AboutHandler

**Since:** 9
**See Also:** Desktop.setAboutHandler(java.awt.desktop.AboutHandler)

---

#### APP_ABOUT

public static final

Desktop.Action

APP_ABOUT

Represents an AboutHandler

APP_PREFERENCES

```java
public static final
Desktop.Action
APP_PREFERENCES
```

Represents a PreferencesHandler

**Since:** 9
**See Also:** Desktop.setPreferencesHandler(java.awt.desktop.PreferencesHandler)

---

#### APP_PREFERENCES

public static final

Desktop.Action

APP_PREFERENCES

Represents a PreferencesHandler

APP_OPEN_FILE

```java
public static final
Desktop.Action
APP_OPEN_FILE
```

Represents an OpenFilesHandler

**Since:** 9
**See Also:** Desktop.setOpenFileHandler(java.awt.desktop.OpenFilesHandler)

---

#### APP_OPEN_FILE

public static final

Desktop.Action

APP_OPEN_FILE

Represents an OpenFilesHandler

APP_PRINT_FILE

```java
public static final
Desktop.Action
APP_PRINT_FILE
```

Represents a PrintFilesHandler

**Since:** 9
**See Also:** Desktop.setPrintFileHandler(java.awt.desktop.PrintFilesHandler)

---

#### APP_PRINT_FILE

public static final

Desktop.Action

APP_PRINT_FILE

Represents a PrintFilesHandler

APP_OPEN_URI

```java
public static final
Desktop.Action
APP_OPEN_URI
```

Represents an OpenURIHandler

**Since:** 9
**See Also:** Desktop.setOpenURIHandler(java.awt.desktop.OpenURIHandler)

---

#### APP_OPEN_URI

public static final

Desktop.Action

APP_OPEN_URI

Represents an OpenURIHandler

APP_QUIT_HANDLER

```java
public static final
Desktop.Action
APP_QUIT_HANDLER
```

Represents a QuitHandler

**Since:** 9
**See Also:** Desktop.setQuitHandler(java.awt.desktop.QuitHandler)

---

#### APP_QUIT_HANDLER

public static final

Desktop.Action

APP_QUIT_HANDLER

Represents a QuitHandler

APP_QUIT_STRATEGY

```java
public static final
Desktop.Action
APP_QUIT_STRATEGY
```

Represents a QuitStrategy

**Since:** 9
**See Also:** Desktop.setQuitStrategy(java.awt.desktop.QuitStrategy)

---

#### APP_QUIT_STRATEGY

public static final

Desktop.Action

APP_QUIT_STRATEGY

Represents a QuitStrategy

APP_SUDDEN_TERMINATION

```java
public static final
Desktop.Action
APP_SUDDEN_TERMINATION
```

Represents a SuddenTermination

**Since:** 9
**See Also:** Desktop.enableSuddenTermination()

---

#### APP_SUDDEN_TERMINATION

public static final

Desktop.Action

APP_SUDDEN_TERMINATION

Represents a SuddenTermination

APP_REQUEST_FOREGROUND

```java
public static final
Desktop.Action
APP_REQUEST_FOREGROUND
```

Represents a requestForeground

**Since:** 9
**See Also:** Desktop.requestForeground(boolean)

---

#### APP_REQUEST_FOREGROUND

public static final

Desktop.Action

APP_REQUEST_FOREGROUND

Represents a requestForeground

APP_HELP_VIEWER

```java
public static final
Desktop.Action
APP_HELP_VIEWER
```

Represents a HelpViewer

**Since:** 9
**See Also:** Desktop.openHelpViewer()

---

#### APP_HELP_VIEWER

public static final

Desktop.Action

APP_HELP_VIEWER

Represents a HelpViewer

APP_MENU_BAR

```java
public static final
Desktop.Action
APP_MENU_BAR
```

Represents a menu bar

**Since:** 9
**See Also:** Desktop.setDefaultMenuBar(javax.swing.JMenuBar)

---

#### APP_MENU_BAR

public static final

Desktop.Action

APP_MENU_BAR

Represents a menu bar

BROWSE_FILE_DIR

```java
public static final
Desktop.Action
BROWSE_FILE_DIR
```

Represents a browse file directory

**Since:** 9
**See Also:** Desktop.browseFileDirectory(java.io.File)

---

#### BROWSE_FILE_DIR

public static final

Desktop.Action

BROWSE_FILE_DIR

Represents a browse file directory

MOVE_TO_TRASH

```java
public static final
Desktop.Action
MOVE_TO_TRASH
```

Represents a move to trash

**Since:** 9
**See Also:** Desktop.moveToTrash(java.io.File)

---

#### MOVE_TO_TRASH

public static final

Desktop.Action

MOVE_TO_TRASH

Represents a move to trash

Method Detail

- values

```java
public static
Desktop.Action
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Desktop.Action c : Desktop.Action.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
Desktop.Action
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### Method Detail

values

```java
public static
Desktop.Action
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Desktop.Action c : Desktop.Action.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

Desktop.Action

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (Desktop.Action c : Desktop.Action.values())
System.out.println(c);
```

for (Desktop.Action c : Desktop.Action.values())
System.out.println(c);

valueOf

```java
public static
Desktop.Action
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### valueOf

public static

Desktop.Action

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

---

