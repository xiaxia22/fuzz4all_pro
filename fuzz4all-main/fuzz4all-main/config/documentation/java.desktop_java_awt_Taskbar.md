# Class Taskbar

**Source:** `java.desktop\java\awt\Taskbar.html`

### Class Description

```java
public class
Taskbar

extends
Object
```

The

Taskbar

class allows a Java application to interact with
the system task area (taskbar, Dock, etc.).

There are a variety of interactions depending on the current platform such as
displaying progress of some task, appending user-specified menu to the application
icon context menu, etc.

**Implementation Note:** Linux support is currently limited to Unity. However to make these
features work on Unity, the app should be run from a .desktop file with
specified

java.desktop.appName

system property set to this .desktop
file name:

Exec=java -Djava.desktop.appName=MyApp.desktop -jar /path/to/myapp.jar

see

https://help.ubuntu.com/community/UnityLaunchersAndDesktopFiles
**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public boolean isSupported​(
Taskbar.Feature
feature)

Tests whether a

Feature

is supported on the current platform.

**Parameters:**
- feature

- the specified

Taskbar.Feature

**Returns:**
- true if the specified feature is supported on the current platform

---

#### public static
Taskbar
getTaskbar()

Returns the

Taskbar

instance of the current
taskbar context. On some platforms the Taskbar API may not be
supported; use the

isTaskbarSupported()

method to
determine if the current taskbar is supported.

**Returns:**
- the Taskbar instance

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
- isTaskbarSupported()

,

GraphicsEnvironment.isHeadless()

---

#### public static boolean isTaskbarSupported()

Tests whether this class is supported on the current platform.
If it's supported, use

getTaskbar()

to retrieve an
instance.

**Returns:**
- true

if this class is supported on the
current platform;

false

otherwise

**See Also:**
- getTaskbar()

---

#### public void requestUserAttention​(boolean enabled,
boolean critical)

Requests user attention to this application.

Depending on the platform, this may be visually indicated by a bouncing
or flashing icon in the task area. It may have no effect on an already active
application.

On some platforms (e.g. Mac OS) this effect may disappear upon app activation
and cannot be dismissed by setting

enabled

to false.
Other platforms may require an additional call

requestUserAttention(boolean, boolean)

to dismiss this request
with

enabled

parameter set to false.

**Parameters:**
- enabled

- disables this request if false
- critical

- if this is an important request

**Throws:**
- SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
- UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.USER_ATTENTION

feature

---

#### public void requestWindowUserAttention​(
Window
w)

Requests user attention to the specified window.

Has no effect if a window representation is not displayable in
the task area. Whether it is displayable is dependent on all
of window type, platform, and implementation.

**Parameters:**
- w

- window

**Throws:**
- SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
- UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.USER_ATTENTION_WINDOW

feature

---

#### public void setMenu​(
PopupMenu
menu)

Attaches the contents of the provided PopupMenu to the application icon
in the task area.

**Parameters:**
- menu

- the PopupMenu to attach to this application

**Throws:**
- SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
- UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.MENU

feature

---

#### public
PopupMenu
getMenu()

Gets PopupMenu used to add items to this application's icon in system task area.

**Returns:**
- the PopupMenu

**Throws:**
- SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
- UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.MENU

feature

---

#### public void setIconImage​(
Image
image)

Changes this application's icon to the provided image.

**Parameters:**
- image

- to change

**Throws:**
- SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
- UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.ICON_IMAGE

feature

---

#### public
Image
getIconImage()

Obtains an image of this application's icon.

**Returns:**
- an image of this application's icon

**Throws:**
- SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
- UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.ICON_IMAGE

feature

---

#### public void setIconBadge​(
String
badge)

Affixes a small system-provided badge to this application's icon.
Usually a number.

Some platforms do not support string values and accept only integer
values. In this case, pass an integer represented as a string as parameter.
This can be tested by

Feature.ICON_BADGE_TEXT

and

Feature.ICON_BADGE_NUMBER

.

Passing

null

as parameter hides the badge.

**Parameters:**
- badge

- label to affix to the icon

**Throws:**
- SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
- UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.ICON_BADGE_NUMBER

or

Taskbar.Feature.ICON_BADGE_TEXT

feature

---

#### public void setWindowIconBadge​(
Window
w,

Image
badge)

Affixes a small badge to this application's icon in the task area
for the specified window.
It may be disabled by system settings.

Has no effect if a window representation is not displayable in
the task area. Whether it is displayable is dependent on all
of window type, platform, and implementation.

**Parameters:**
- w

- window to update
- badge

- image to affix to the icon

**Throws:**
- SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
- UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.ICON_BADGE_IMAGE_WINDOW

feature

---

#### public void setProgressValue​(int value)

Affixes a small system-provided progress bar to this application's icon.

**Parameters:**
- value

- from 0 to 100, other to disable progress indication

**Throws:**
- SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
- UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.PROGRESS_VALUE

feature

---

#### public void setWindowProgressValue​(
Window
w,
int value)

Displays a determinate progress bar in the task area for the specified
window.

Has no effect if a window representation is not displayable in
the task area. Whether it is displayable is dependent on all
of window type, platform, and implementation.

The visual behavior is platform and

Taskbar.State

dependent.

This call cancels the

INDETERMINATE

state
of the window.

Note that when multiple windows is grouped in the task area
the behavior is platform specific.

**Parameters:**
- w

- window to update
- value

- from 0 to 100, other to switch to

Taskbar.State.OFF

state
and disable progress indication

**Throws:**
- SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
- UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.PROGRESS_VALUE_WINDOW

feature

**See Also:**
- setWindowProgressState(java.awt.Window, State)

---

#### public void setWindowProgressState​(
Window
w,

Taskbar.State
state)

Sets a progress state for a specified window.

Has no effect if a window representation is not displayable in
the task area. Whether it is displayable is dependent on all
of window type, platform, and implementation.

Each state displays a progress in a platform-dependent way.

Note than switching from

INDETERMINATE

state
to any of determinate states may reset value set by

setWindowProgressValue

**Parameters:**
- w

- window
- state

- to change to

**Throws:**
- SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
- UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.PROGRESS_STATE_WINDOW

feature

**See Also:**
- Taskbar.State.OFF

,

Taskbar.State.NORMAL

,

Taskbar.State.PAUSED

,

Taskbar.State.ERROR

,

Taskbar.State.INDETERMINATE

,

setWindowProgressValue(java.awt.Window, int)

---

### Additional Sections

#### Class Taskbar

java.lang.Object

- java.awt.Taskbar

java.awt.Taskbar

```java
public class
Taskbar

extends
Object
```

The

Taskbar

class allows a Java application to interact with
the system task area (taskbar, Dock, etc.).

There are a variety of interactions depending on the current platform such as
displaying progress of some task, appending user-specified menu to the application
icon context menu, etc.

**Implementation Note:** Linux support is currently limited to Unity. However to make these
features work on Unity, the app should be run from a .desktop file with
specified

java.desktop.appName

system property set to this .desktop
file name:

Exec=java -Djava.desktop.appName=MyApp.desktop -jar /path/to/myapp.jar

see

https://help.ubuntu.com/community/UnityLaunchersAndDesktopFiles
**Since:** 9

public class

Taskbar

extends

Object

The

Taskbar

class allows a Java application to interact with
the system task area (taskbar, Dock, etc.).

There are a variety of interactions depending on the current platform such as
displaying progress of some task, appending user-specified menu to the application
icon context menu, etc.

There are a variety of interactions depending on the current platform such as
displaying progress of some task, appending user-specified menu to the application
icon context menu, etc.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Taskbar.Feature

List of provided features.

static class

Taskbar.State

Kinds of available window progress states.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Image

getIconImage

()

Obtains an image of this application's icon.

PopupMenu

getMenu

()

Gets PopupMenu used to add items to this application's icon in system task area.

static

Taskbar

getTaskbar

()

Returns the

Taskbar

instance of the current
taskbar context.

boolean

isSupported

​(

Taskbar.Feature

feature)

Tests whether a

Feature

is supported on the current platform.

static boolean

isTaskbarSupported

()

Tests whether this class is supported on the current platform.

void

requestUserAttention

​(boolean enabled,
boolean critical)

Requests user attention to this application.

void

requestWindowUserAttention

​(

Window

w)

Requests user attention to the specified window.

void

setIconBadge

​(

String

badge)

Affixes a small system-provided badge to this application's icon.

void

setIconImage

​(

Image

image)

Changes this application's icon to the provided image.

void

setMenu

​(

PopupMenu

menu)

Attaches the contents of the provided PopupMenu to the application icon
in the task area.

void

setProgressValue

​(int value)

Affixes a small system-provided progress bar to this application's icon.

void

setWindowIconBadge

​(

Window

w,

Image

badge)

Affixes a small badge to this application's icon in the task area
for the specified window.

void

setWindowProgressState

​(

Window

w,

Taskbar.State

state)

Sets a progress state for a specified window.

void

setWindowProgressValue

​(

Window

w,
int value)

Displays a determinate progress bar in the task area for the specified
window.

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

Taskbar.Feature

List of provided features.

static class

Taskbar.State

Kinds of available window progress states.

---

#### Nested Class Summary

List of provided features.

Kinds of available window progress states.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Image

getIconImage

()

Obtains an image of this application's icon.

PopupMenu

getMenu

()

Gets PopupMenu used to add items to this application's icon in system task area.

static

Taskbar

getTaskbar

()

Returns the

Taskbar

instance of the current
taskbar context.

boolean

isSupported

​(

Taskbar.Feature

feature)

Tests whether a

Feature

is supported on the current platform.

static boolean

isTaskbarSupported

()

Tests whether this class is supported on the current platform.

void

requestUserAttention

​(boolean enabled,
boolean critical)

Requests user attention to this application.

void

requestWindowUserAttention

​(

Window

w)

Requests user attention to the specified window.

void

setIconBadge

​(

String

badge)

Affixes a small system-provided badge to this application's icon.

void

setIconImage

​(

Image

image)

Changes this application's icon to the provided image.

void

setMenu

​(

PopupMenu

menu)

Attaches the contents of the provided PopupMenu to the application icon
in the task area.

void

setProgressValue

​(int value)

Affixes a small system-provided progress bar to this application's icon.

void

setWindowIconBadge

​(

Window

w,

Image

badge)

Affixes a small badge to this application's icon in the task area
for the specified window.

void

setWindowProgressState

​(

Window

w,

Taskbar.State

state)

Sets a progress state for a specified window.

void

setWindowProgressValue

​(

Window

w,
int value)

Displays a determinate progress bar in the task area for the specified
window.

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

Obtains an image of this application's icon.

Gets PopupMenu used to add items to this application's icon in system task area.

Returns the

Taskbar

instance of the current
taskbar context.

Tests whether a

Feature

is supported on the current platform.

Tests whether this class is supported on the current platform.

Requests user attention to this application.

Requests user attention to the specified window.

Affixes a small system-provided badge to this application's icon.

Changes this application's icon to the provided image.

Attaches the contents of the provided PopupMenu to the application icon
in the task area.

Affixes a small system-provided progress bar to this application's icon.

Affixes a small badge to this application's icon in the task area
for the specified window.

Sets a progress state for a specified window.

Displays a determinate progress bar in the task area for the specified
window.

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

- isSupported

```java
public boolean isSupported​(
Taskbar.Feature
feature)
```

Tests whether a

Feature

is supported on the current platform.

**Parameters:** feature

- the specified

Taskbar.Feature
**Returns:** true if the specified feature is supported on the current platform

- getTaskbar

```java
public static
Taskbar
getTaskbar()
```

Returns the

Taskbar

instance of the current
taskbar context. On some platforms the Taskbar API may not be
supported; use the

isTaskbarSupported()

method to
determine if the current taskbar is supported.

**Returns:** the Taskbar instance
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** UnsupportedOperationException

- if this class is not
supported on the current platform
**See Also:** isTaskbarSupported()

,

GraphicsEnvironment.isHeadless()

- isTaskbarSupported

```java
public static boolean isTaskbarSupported()
```

Tests whether this class is supported on the current platform.
If it's supported, use

getTaskbar()

to retrieve an
instance.

**Returns:** true

if this class is supported on the
current platform;

false

otherwise
**See Also:** getTaskbar()

- requestUserAttention

```java
public void requestUserAttention​(boolean enabled,
boolean critical)
```

Requests user attention to this application.

Depending on the platform, this may be visually indicated by a bouncing
or flashing icon in the task area. It may have no effect on an already active
application.

On some platforms (e.g. Mac OS) this effect may disappear upon app activation
and cannot be dismissed by setting

enabled

to false.
Other platforms may require an additional call

requestUserAttention(boolean, boolean)

to dismiss this request
with

enabled

parameter set to false.

**Parameters:** enabled

- disables this request if false
**Parameters:** critical

- if this is an important request
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.USER_ATTENTION

feature

- requestWindowUserAttention

```java
public void requestWindowUserAttention​(
Window
w)
```

Requests user attention to the specified window.

Has no effect if a window representation is not displayable in
the task area. Whether it is displayable is dependent on all
of window type, platform, and implementation.

**Parameters:** w

- window
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.USER_ATTENTION_WINDOW

feature

- setMenu

```java
public void setMenu​(
PopupMenu
menu)
```

Attaches the contents of the provided PopupMenu to the application icon
in the task area.

**Parameters:** menu

- the PopupMenu to attach to this application
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.MENU

feature

- getMenu

```java
public
PopupMenu
getMenu()
```

Gets PopupMenu used to add items to this application's icon in system task area.

**Returns:** the PopupMenu
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.MENU

feature

- setIconImage

```java
public void setIconImage​(
Image
image)
```

Changes this application's icon to the provided image.

**Parameters:** image

- to change
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.ICON_IMAGE

feature

- getIconImage

```java
public
Image
getIconImage()
```

Obtains an image of this application's icon.

**Returns:** an image of this application's icon
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.ICON_IMAGE

feature

- setIconBadge

```java
public void setIconBadge​(
String
badge)
```

Affixes a small system-provided badge to this application's icon.
Usually a number.

Some platforms do not support string values and accept only integer
values. In this case, pass an integer represented as a string as parameter.
This can be tested by

Feature.ICON_BADGE_TEXT

and

Feature.ICON_BADGE_NUMBER

.

Passing

null

as parameter hides the badge.

**Parameters:** badge

- label to affix to the icon
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.ICON_BADGE_NUMBER

or

Taskbar.Feature.ICON_BADGE_TEXT

feature

- setWindowIconBadge

```java
public void setWindowIconBadge​(
Window
w,

Image
badge)
```

Affixes a small badge to this application's icon in the task area
for the specified window.
It may be disabled by system settings.

Has no effect if a window representation is not displayable in
the task area. Whether it is displayable is dependent on all
of window type, platform, and implementation.

**Parameters:** w

- window to update
**Parameters:** badge

- image to affix to the icon
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.ICON_BADGE_IMAGE_WINDOW

feature

- setProgressValue

```java
public void setProgressValue​(int value)
```

Affixes a small system-provided progress bar to this application's icon.

**Parameters:** value

- from 0 to 100, other to disable progress indication
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.PROGRESS_VALUE

feature

- setWindowProgressValue

```java
public void setWindowProgressValue​(
Window
w,
int value)
```

Displays a determinate progress bar in the task area for the specified
window.

Has no effect if a window representation is not displayable in
the task area. Whether it is displayable is dependent on all
of window type, platform, and implementation.

The visual behavior is platform and

Taskbar.State

dependent.

This call cancels the

INDETERMINATE

state
of the window.

Note that when multiple windows is grouped in the task area
the behavior is platform specific.

**Parameters:** w

- window to update
**Parameters:** value

- from 0 to 100, other to switch to

Taskbar.State.OFF

state
and disable progress indication
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.PROGRESS_VALUE_WINDOW

feature
**See Also:** setWindowProgressState(java.awt.Window, State)

- setWindowProgressState

```java
public void setWindowProgressState​(
Window
w,

Taskbar.State
state)
```

Sets a progress state for a specified window.

Has no effect if a window representation is not displayable in
the task area. Whether it is displayable is dependent on all
of window type, platform, and implementation.

Each state displays a progress in a platform-dependent way.

Note than switching from

INDETERMINATE

state
to any of determinate states may reset value set by

setWindowProgressValue

**Parameters:** w

- window
**Parameters:** state

- to change to
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.PROGRESS_STATE_WINDOW

feature
**See Also:** Taskbar.State.OFF

,

Taskbar.State.NORMAL

,

Taskbar.State.PAUSED

,

Taskbar.State.ERROR

,

Taskbar.State.INDETERMINATE

,

setWindowProgressValue(java.awt.Window, int)

Method Detail

- isSupported

```java
public boolean isSupported​(
Taskbar.Feature
feature)
```

Tests whether a

Feature

is supported on the current platform.

**Parameters:** feature

- the specified

Taskbar.Feature
**Returns:** true if the specified feature is supported on the current platform

- getTaskbar

```java
public static
Taskbar
getTaskbar()
```

Returns the

Taskbar

instance of the current
taskbar context. On some platforms the Taskbar API may not be
supported; use the

isTaskbarSupported()

method to
determine if the current taskbar is supported.

**Returns:** the Taskbar instance
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** UnsupportedOperationException

- if this class is not
supported on the current platform
**See Also:** isTaskbarSupported()

,

GraphicsEnvironment.isHeadless()

- isTaskbarSupported

```java
public static boolean isTaskbarSupported()
```

Tests whether this class is supported on the current platform.
If it's supported, use

getTaskbar()

to retrieve an
instance.

**Returns:** true

if this class is supported on the
current platform;

false

otherwise
**See Also:** getTaskbar()

- requestUserAttention

```java
public void requestUserAttention​(boolean enabled,
boolean critical)
```

Requests user attention to this application.

Depending on the platform, this may be visually indicated by a bouncing
or flashing icon in the task area. It may have no effect on an already active
application.

On some platforms (e.g. Mac OS) this effect may disappear upon app activation
and cannot be dismissed by setting

enabled

to false.
Other platforms may require an additional call

requestUserAttention(boolean, boolean)

to dismiss this request
with

enabled

parameter set to false.

**Parameters:** enabled

- disables this request if false
**Parameters:** critical

- if this is an important request
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.USER_ATTENTION

feature

- requestWindowUserAttention

```java
public void requestWindowUserAttention​(
Window
w)
```

Requests user attention to the specified window.

Has no effect if a window representation is not displayable in
the task area. Whether it is displayable is dependent on all
of window type, platform, and implementation.

**Parameters:** w

- window
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.USER_ATTENTION_WINDOW

feature

- setMenu

```java
public void setMenu​(
PopupMenu
menu)
```

Attaches the contents of the provided PopupMenu to the application icon
in the task area.

**Parameters:** menu

- the PopupMenu to attach to this application
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.MENU

feature

- getMenu

```java
public
PopupMenu
getMenu()
```

Gets PopupMenu used to add items to this application's icon in system task area.

**Returns:** the PopupMenu
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.MENU

feature

- setIconImage

```java
public void setIconImage​(
Image
image)
```

Changes this application's icon to the provided image.

**Parameters:** image

- to change
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.ICON_IMAGE

feature

- getIconImage

```java
public
Image
getIconImage()
```

Obtains an image of this application's icon.

**Returns:** an image of this application's icon
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.ICON_IMAGE

feature

- setIconBadge

```java
public void setIconBadge​(
String
badge)
```

Affixes a small system-provided badge to this application's icon.
Usually a number.

Some platforms do not support string values and accept only integer
values. In this case, pass an integer represented as a string as parameter.
This can be tested by

Feature.ICON_BADGE_TEXT

and

Feature.ICON_BADGE_NUMBER

.

Passing

null

as parameter hides the badge.

**Parameters:** badge

- label to affix to the icon
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.ICON_BADGE_NUMBER

or

Taskbar.Feature.ICON_BADGE_TEXT

feature

- setWindowIconBadge

```java
public void setWindowIconBadge​(
Window
w,

Image
badge)
```

Affixes a small badge to this application's icon in the task area
for the specified window.
It may be disabled by system settings.

Has no effect if a window representation is not displayable in
the task area. Whether it is displayable is dependent on all
of window type, platform, and implementation.

**Parameters:** w

- window to update
**Parameters:** badge

- image to affix to the icon
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.ICON_BADGE_IMAGE_WINDOW

feature

- setProgressValue

```java
public void setProgressValue​(int value)
```

Affixes a small system-provided progress bar to this application's icon.

**Parameters:** value

- from 0 to 100, other to disable progress indication
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.PROGRESS_VALUE

feature

- setWindowProgressValue

```java
public void setWindowProgressValue​(
Window
w,
int value)
```

Displays a determinate progress bar in the task area for the specified
window.

Has no effect if a window representation is not displayable in
the task area. Whether it is displayable is dependent on all
of window type, platform, and implementation.

The visual behavior is platform and

Taskbar.State

dependent.

This call cancels the

INDETERMINATE

state
of the window.

Note that when multiple windows is grouped in the task area
the behavior is platform specific.

**Parameters:** w

- window to update
**Parameters:** value

- from 0 to 100, other to switch to

Taskbar.State.OFF

state
and disable progress indication
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.PROGRESS_VALUE_WINDOW

feature
**See Also:** setWindowProgressState(java.awt.Window, State)

- setWindowProgressState

```java
public void setWindowProgressState​(
Window
w,

Taskbar.State
state)
```

Sets a progress state for a specified window.

Has no effect if a window representation is not displayable in
the task area. Whether it is displayable is dependent on all
of window type, platform, and implementation.

Each state displays a progress in a platform-dependent way.

Note than switching from

INDETERMINATE

state
to any of determinate states may reset value set by

setWindowProgressValue

**Parameters:** w

- window
**Parameters:** state

- to change to
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.PROGRESS_STATE_WINDOW

feature
**See Also:** Taskbar.State.OFF

,

Taskbar.State.NORMAL

,

Taskbar.State.PAUSED

,

Taskbar.State.ERROR

,

Taskbar.State.INDETERMINATE

,

setWindowProgressValue(java.awt.Window, int)

---

#### Method Detail

isSupported

```java
public boolean isSupported​(
Taskbar.Feature
feature)
```

Tests whether a

Feature

is supported on the current platform.

**Parameters:** feature

- the specified

Taskbar.Feature
**Returns:** true if the specified feature is supported on the current platform

---

#### isSupported

public boolean isSupported​(

Taskbar.Feature

feature)

Tests whether a

Feature

is supported on the current platform.

getTaskbar

```java
public static
Taskbar
getTaskbar()
```

Returns the

Taskbar

instance of the current
taskbar context. On some platforms the Taskbar API may not be
supported; use the

isTaskbarSupported()

method to
determine if the current taskbar is supported.

**Returns:** the Taskbar instance
**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** UnsupportedOperationException

- if this class is not
supported on the current platform
**See Also:** isTaskbarSupported()

,

GraphicsEnvironment.isHeadless()

---

#### getTaskbar

public static

Taskbar

getTaskbar()

Returns the

Taskbar

instance of the current
taskbar context. On some platforms the Taskbar API may not be
supported; use the

isTaskbarSupported()

method to
determine if the current taskbar is supported.

isTaskbarSupported

```java
public static boolean isTaskbarSupported()
```

Tests whether this class is supported on the current platform.
If it's supported, use

getTaskbar()

to retrieve an
instance.

**Returns:** true

if this class is supported on the
current platform;

false

otherwise
**See Also:** getTaskbar()

---

#### isTaskbarSupported

public static boolean isTaskbarSupported()

Tests whether this class is supported on the current platform.
If it's supported, use

getTaskbar()

to retrieve an
instance.

requestUserAttention

```java
public void requestUserAttention​(boolean enabled,
boolean critical)
```

Requests user attention to this application.

Depending on the platform, this may be visually indicated by a bouncing
or flashing icon in the task area. It may have no effect on an already active
application.

On some platforms (e.g. Mac OS) this effect may disappear upon app activation
and cannot be dismissed by setting

enabled

to false.
Other platforms may require an additional call

requestUserAttention(boolean, boolean)

to dismiss this request
with

enabled

parameter set to false.

**Parameters:** enabled

- disables this request if false
**Parameters:** critical

- if this is an important request
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.USER_ATTENTION

feature

---

#### requestUserAttention

public void requestUserAttention​(boolean enabled,
boolean critical)

Requests user attention to this application.

Depending on the platform, this may be visually indicated by a bouncing
or flashing icon in the task area. It may have no effect on an already active
application.

On some platforms (e.g. Mac OS) this effect may disappear upon app activation
and cannot be dismissed by setting

enabled

to false.
Other platforms may require an additional call

requestUserAttention(boolean, boolean)

to dismiss this request
with

enabled

parameter set to false.

requestWindowUserAttention

```java
public void requestWindowUserAttention​(
Window
w)
```

Requests user attention to the specified window.

Has no effect if a window representation is not displayable in
the task area. Whether it is displayable is dependent on all
of window type, platform, and implementation.

**Parameters:** w

- window
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.USER_ATTENTION_WINDOW

feature

---

#### requestWindowUserAttention

public void requestWindowUserAttention​(

Window

w)

Requests user attention to the specified window.

Has no effect if a window representation is not displayable in
the task area. Whether it is displayable is dependent on all
of window type, platform, and implementation.

setMenu

```java
public void setMenu​(
PopupMenu
menu)
```

Attaches the contents of the provided PopupMenu to the application icon
in the task area.

**Parameters:** menu

- the PopupMenu to attach to this application
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.MENU

feature

---

#### setMenu

public void setMenu​(

PopupMenu

menu)

Attaches the contents of the provided PopupMenu to the application icon
in the task area.

getMenu

```java
public
PopupMenu
getMenu()
```

Gets PopupMenu used to add items to this application's icon in system task area.

**Returns:** the PopupMenu
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.MENU

feature

---

#### getMenu

public

PopupMenu

getMenu()

Gets PopupMenu used to add items to this application's icon in system task area.

setIconImage

```java
public void setIconImage​(
Image
image)
```

Changes this application's icon to the provided image.

**Parameters:** image

- to change
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.ICON_IMAGE

feature

---

#### setIconImage

public void setIconImage​(

Image

image)

Changes this application's icon to the provided image.

getIconImage

```java
public
Image
getIconImage()
```

Obtains an image of this application's icon.

**Returns:** an image of this application's icon
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.ICON_IMAGE

feature

---

#### getIconImage

public

Image

getIconImage()

Obtains an image of this application's icon.

setIconBadge

```java
public void setIconBadge​(
String
badge)
```

Affixes a small system-provided badge to this application's icon.
Usually a number.

Some platforms do not support string values and accept only integer
values. In this case, pass an integer represented as a string as parameter.
This can be tested by

Feature.ICON_BADGE_TEXT

and

Feature.ICON_BADGE_NUMBER

.

Passing

null

as parameter hides the badge.

**Parameters:** badge

- label to affix to the icon
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.ICON_BADGE_NUMBER

or

Taskbar.Feature.ICON_BADGE_TEXT

feature

---

#### setIconBadge

public void setIconBadge​(

String

badge)

Affixes a small system-provided badge to this application's icon.
Usually a number.

Some platforms do not support string values and accept only integer
values. In this case, pass an integer represented as a string as parameter.
This can be tested by

Feature.ICON_BADGE_TEXT

and

Feature.ICON_BADGE_NUMBER

.

Passing

null

as parameter hides the badge.

setWindowIconBadge

```java
public void setWindowIconBadge​(
Window
w,

Image
badge)
```

Affixes a small badge to this application's icon in the task area
for the specified window.
It may be disabled by system settings.

Has no effect if a window representation is not displayable in
the task area. Whether it is displayable is dependent on all
of window type, platform, and implementation.

**Parameters:** w

- window to update
**Parameters:** badge

- image to affix to the icon
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.ICON_BADGE_IMAGE_WINDOW

feature

---

#### setWindowIconBadge

public void setWindowIconBadge​(

Window

w,

Image

badge)

Affixes a small badge to this application's icon in the task area
for the specified window.
It may be disabled by system settings.

Has no effect if a window representation is not displayable in
the task area. Whether it is displayable is dependent on all
of window type, platform, and implementation.

setProgressValue

```java
public void setProgressValue​(int value)
```

Affixes a small system-provided progress bar to this application's icon.

**Parameters:** value

- from 0 to 100, other to disable progress indication
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.PROGRESS_VALUE

feature

---

#### setProgressValue

public void setProgressValue​(int value)

Affixes a small system-provided progress bar to this application's icon.

setWindowProgressValue

```java
public void setWindowProgressValue​(
Window
w,
int value)
```

Displays a determinate progress bar in the task area for the specified
window.

Has no effect if a window representation is not displayable in
the task area. Whether it is displayable is dependent on all
of window type, platform, and implementation.

The visual behavior is platform and

Taskbar.State

dependent.

This call cancels the

INDETERMINATE

state
of the window.

Note that when multiple windows is grouped in the task area
the behavior is platform specific.

**Parameters:** w

- window to update
**Parameters:** value

- from 0 to 100, other to switch to

Taskbar.State.OFF

state
and disable progress indication
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.PROGRESS_VALUE_WINDOW

feature
**See Also:** setWindowProgressState(java.awt.Window, State)

---

#### setWindowProgressValue

public void setWindowProgressValue​(

Window

w,
int value)

Displays a determinate progress bar in the task area for the specified
window.

Has no effect if a window representation is not displayable in
the task area. Whether it is displayable is dependent on all
of window type, platform, and implementation.

The visual behavior is platform and

Taskbar.State

dependent.

This call cancels the

INDETERMINATE

state
of the window.

Note that when multiple windows is grouped in the task area
the behavior is platform specific.

setWindowProgressState

```java
public void setWindowProgressState​(
Window
w,

Taskbar.State
state)
```

Sets a progress state for a specified window.

Has no effect if a window representation is not displayable in
the task area. Whether it is displayable is dependent on all
of window type, platform, and implementation.

Each state displays a progress in a platform-dependent way.

Note than switching from

INDETERMINATE

state
to any of determinate states may reset value set by

setWindowProgressValue

**Parameters:** w

- window
**Parameters:** state

- to change to
**Throws:** SecurityException

- if a security manager exists and it denies the

RuntimePermission("canProcessApplicationEvents")

permission.
**Throws:** UnsupportedOperationException

- if the current platform
does not support the

Taskbar.Feature.PROGRESS_STATE_WINDOW

feature
**See Also:** Taskbar.State.OFF

,

Taskbar.State.NORMAL

,

Taskbar.State.PAUSED

,

Taskbar.State.ERROR

,

Taskbar.State.INDETERMINATE

,

setWindowProgressValue(java.awt.Window, int)

---

#### setWindowProgressState

public void setWindowProgressState​(

Window

w,

Taskbar.State

state)

Sets a progress state for a specified window.

Has no effect if a window representation is not displayable in
the task area. Whether it is displayable is dependent on all
of window type, platform, and implementation.

Each state displays a progress in a platform-dependent way.

Note than switching from

INDETERMINATE

state
to any of determinate states may reset value set by

setWindowProgressValue

---

