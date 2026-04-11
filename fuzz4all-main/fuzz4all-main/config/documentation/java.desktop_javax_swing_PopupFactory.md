# Class PopupFactory

**Source:** `java.desktop\javax\swing\PopupFactory.html`

### Class Description

```java
public class
PopupFactory

extends
Object
```

PopupFactory

, as the name implies, is used to obtain
instances of

Popup

s.

Popup

s are used to
display a

Component

above all other

Component

s
in a particular containment hierarchy. The general contract is that
once you have obtained a

Popup

from a

PopupFactory

, you must invoke

hide

on the

Popup

. The typical usage is:

```java
PopupFactory factory = PopupFactory.getSharedInstance();
Popup popup = factory.getPopup(owner, contents, x, y);
popup.show();
...
popup.hide();
```

**Since:** 1.4
**See Also:** Popup

---

### Field Details

*No entries found.*

### Constructor Details

#### public PopupFactory()

*No description found.*

---

### Method Details

#### public static void setSharedInstance​(
PopupFactory
factory)

Sets the

PopupFactory

that will be used to obtain

Popup

s.
This will throw an

IllegalArgumentException

if

factory

is null.

**Parameters:**
- factory

- Shared PopupFactory

**Throws:**
- IllegalArgumentException

- if

factory

is null

**See Also:**
- getPopup(java.awt.Component, java.awt.Component, int, int)

---

#### public static
PopupFactory
getSharedInstance()

Returns the shared

PopupFactory

which can be used
to obtain

Popup

s.

**Returns:**
- Shared PopupFactory

---

#### public
Popup
getPopup​(
Component
owner,

Component
contents,
int x,
int y)
throws
IllegalArgumentException

Creates a

Popup

for the Component

owner

containing the Component

contents

.

owner

is used to determine which

Window

the new

Popup

will parent the

Component

the

Popup

creates to. A null

owner

implies there
is no valid parent.

x

and

y

specify the preferred initial location to place
the

Popup

at. Based on screen size, or other paramaters,
the

Popup

may not display at

x

and

y

.

**Parameters:**
- owner

- Component mouse coordinates are relative to, may be null
- contents

- Contents of the Popup
- x

- Initial x screen coordinate
- y

- Initial y screen coordinate

**Returns:**
- Popup containing Contents

**Throws:**
- IllegalArgumentException

- if contents is null

---

#### protected
Popup
getPopup​(
Component
owner,

Component
contents,
int x,
int y,
boolean isHeavyWeightPopup)
throws
IllegalArgumentException

Creates a

Popup

for the Component

owner

containing the Component

contents

.
The window containing the component

owner

will be used as the parent window. A null

owner

implies there
is no valid parent.

x

and

y

specify the preferred
initial location to place the

Popup

at. Based on screen size,
or other parameters, the

Popup

may not display at

x

and

y

.

isHeavyWeightPopup

specifies if the

Popup

will be heavyweight. Passing

true

will force the

Popup

type to be heavyweight, otherwise

Popup

type will be selected by

Popup

factory. Lightweight

Popup

windows are more
efficient than heavyweight (native peer) windows, but lightweight
and heavyweight components do not mix well in a GUI.
This method is intended to be used only by PopupFactory sub-classes.

**Parameters:**
- owner

- Component mouse coordinates are relative to, may be null
- contents

- Contents of the Popup
- x

- Initial x screen coordinate
- y

- Initial y screen coordinate
- isHeavyWeightPopup

- true if Popup should be heavy weight,
otherwise popup type will be selected by popup factory.

**Returns:**
- Popup containing Contents

**Throws:**
- IllegalArgumentException

- if contents is null

---

### Additional Sections

#### Class PopupFactory

java.lang.Object

- javax.swing.PopupFactory

javax.swing.PopupFactory

```java
public class
PopupFactory

extends
Object
```

PopupFactory

, as the name implies, is used to obtain
instances of

Popup

s.

Popup

s are used to
display a

Component

above all other

Component

s
in a particular containment hierarchy. The general contract is that
once you have obtained a

Popup

from a

PopupFactory

, you must invoke

hide

on the

Popup

. The typical usage is:

```java
PopupFactory factory = PopupFactory.getSharedInstance();
Popup popup = factory.getPopup(owner, contents, x, y);
popup.show();
...
popup.hide();
```

**Since:** 1.4
**See Also:** Popup

public class

PopupFactory

extends

Object

PopupFactory

, as the name implies, is used to obtain
instances of

Popup

s.

Popup

s are used to
display a

Component

above all other

Component

s
in a particular containment hierarchy. The general contract is that
once you have obtained a

Popup

from a

PopupFactory

, you must invoke

hide

on the

Popup

. The typical usage is:

```java
PopupFactory factory = PopupFactory.getSharedInstance();
Popup popup = factory.getPopup(owner, contents, x, y);
popup.show();
...
popup.hide();
```

PopupFactory factory = PopupFactory.getSharedInstance();
Popup popup = factory.getPopup(owner, contents, x, y);
popup.show();
...
popup.hide();

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PopupFactory

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Popup

getPopup

​(

Component

owner,

Component

contents,
int x,
int y)

Creates a

Popup

for the Component

owner

containing the Component

contents

.

protected

Popup

getPopup

​(

Component

owner,

Component

contents,
int x,
int y,
boolean isHeavyWeightPopup)

Creates a

Popup

for the Component

owner

containing the Component

contents

.

static

PopupFactory

getSharedInstance

()

Returns the shared

PopupFactory

which can be used
to obtain

Popup

s.

static void

setSharedInstance

​(

PopupFactory

factory)

Sets the

PopupFactory

that will be used to obtain

Popup

s.

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

Constructor Summary

Constructors

Constructor

Description

PopupFactory

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Popup

getPopup

​(

Component

owner,

Component

contents,
int x,
int y)

Creates a

Popup

for the Component

owner

containing the Component

contents

.

protected

Popup

getPopup

​(

Component

owner,

Component

contents,
int x,
int y,
boolean isHeavyWeightPopup)

Creates a

Popup

for the Component

owner

containing the Component

contents

.

static

PopupFactory

getSharedInstance

()

Returns the shared

PopupFactory

which can be used
to obtain

Popup

s.

static void

setSharedInstance

​(

PopupFactory

factory)

Sets the

PopupFactory

that will be used to obtain

Popup

s.

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

Creates a

Popup

for the Component

owner

containing the Component

contents

.

Returns the shared

PopupFactory

which can be used
to obtain

Popup

s.

Sets the

PopupFactory

that will be used to obtain

Popup

s.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PopupFactory

```java
public PopupFactory()
```

============ METHOD DETAIL ==========

- Method Detail

- setSharedInstance

```java
public static void setSharedInstance​(
PopupFactory
factory)
```

Sets the

PopupFactory

that will be used to obtain

Popup

s.
This will throw an

IllegalArgumentException

if

factory

is null.

**Parameters:** factory

- Shared PopupFactory
**Throws:** IllegalArgumentException

- if

factory

is null
**See Also:** getPopup(java.awt.Component, java.awt.Component, int, int)

- getSharedInstance

```java
public static
PopupFactory
getSharedInstance()
```

Returns the shared

PopupFactory

which can be used
to obtain

Popup

s.

**Returns:** Shared PopupFactory

- getPopup

```java
public
Popup
getPopup​(
Component
owner,

Component
contents,
int x,
int y)
throws
IllegalArgumentException
```

Creates a

Popup

for the Component

owner

containing the Component

contents

.

owner

is used to determine which

Window

the new

Popup

will parent the

Component

the

Popup

creates to. A null

owner

implies there
is no valid parent.

x

and

y

specify the preferred initial location to place
the

Popup

at. Based on screen size, or other paramaters,
the

Popup

may not display at

x

and

y

.

**Parameters:** owner

- Component mouse coordinates are relative to, may be null
**Parameters:** contents

- Contents of the Popup
**Parameters:** x

- Initial x screen coordinate
**Parameters:** y

- Initial y screen coordinate
**Returns:** Popup containing Contents
**Throws:** IllegalArgumentException

- if contents is null

- getPopup

```java
protected
Popup
getPopup​(
Component
owner,

Component
contents,
int x,
int y,
boolean isHeavyWeightPopup)
throws
IllegalArgumentException
```

Creates a

Popup

for the Component

owner

containing the Component

contents

.
The window containing the component

owner

will be used as the parent window. A null

owner

implies there
is no valid parent.

x

and

y

specify the preferred
initial location to place the

Popup

at. Based on screen size,
or other parameters, the

Popup

may not display at

x

and

y

.

isHeavyWeightPopup

specifies if the

Popup

will be heavyweight. Passing

true

will force the

Popup

type to be heavyweight, otherwise

Popup

type will be selected by

Popup

factory. Lightweight

Popup

windows are more
efficient than heavyweight (native peer) windows, but lightweight
and heavyweight components do not mix well in a GUI.
This method is intended to be used only by PopupFactory sub-classes.

**Parameters:** owner

- Component mouse coordinates are relative to, may be null
**Parameters:** contents

- Contents of the Popup
**Parameters:** x

- Initial x screen coordinate
**Parameters:** y

- Initial y screen coordinate
**Parameters:** isHeavyWeightPopup

- true if Popup should be heavy weight,
otherwise popup type will be selected by popup factory.
**Returns:** Popup containing Contents
**Throws:** IllegalArgumentException

- if contents is null

Constructor Detail

- PopupFactory

```java
public PopupFactory()
```

---

#### Constructor Detail

PopupFactory

```java
public PopupFactory()
```

---

#### PopupFactory

public PopupFactory()

Method Detail

- setSharedInstance

```java
public static void setSharedInstance​(
PopupFactory
factory)
```

Sets the

PopupFactory

that will be used to obtain

Popup

s.
This will throw an

IllegalArgumentException

if

factory

is null.

**Parameters:** factory

- Shared PopupFactory
**Throws:** IllegalArgumentException

- if

factory

is null
**See Also:** getPopup(java.awt.Component, java.awt.Component, int, int)

- getSharedInstance

```java
public static
PopupFactory
getSharedInstance()
```

Returns the shared

PopupFactory

which can be used
to obtain

Popup

s.

**Returns:** Shared PopupFactory

- getPopup

```java
public
Popup
getPopup​(
Component
owner,

Component
contents,
int x,
int y)
throws
IllegalArgumentException
```

Creates a

Popup

for the Component

owner

containing the Component

contents

.

owner

is used to determine which

Window

the new

Popup

will parent the

Component

the

Popup

creates to. A null

owner

implies there
is no valid parent.

x

and

y

specify the preferred initial location to place
the

Popup

at. Based on screen size, or other paramaters,
the

Popup

may not display at

x

and

y

.

**Parameters:** owner

- Component mouse coordinates are relative to, may be null
**Parameters:** contents

- Contents of the Popup
**Parameters:** x

- Initial x screen coordinate
**Parameters:** y

- Initial y screen coordinate
**Returns:** Popup containing Contents
**Throws:** IllegalArgumentException

- if contents is null

- getPopup

```java
protected
Popup
getPopup​(
Component
owner,

Component
contents,
int x,
int y,
boolean isHeavyWeightPopup)
throws
IllegalArgumentException
```

Creates a

Popup

for the Component

owner

containing the Component

contents

.
The window containing the component

owner

will be used as the parent window. A null

owner

implies there
is no valid parent.

x

and

y

specify the preferred
initial location to place the

Popup

at. Based on screen size,
or other parameters, the

Popup

may not display at

x

and

y

.

isHeavyWeightPopup

specifies if the

Popup

will be heavyweight. Passing

true

will force the

Popup

type to be heavyweight, otherwise

Popup

type will be selected by

Popup

factory. Lightweight

Popup

windows are more
efficient than heavyweight (native peer) windows, but lightweight
and heavyweight components do not mix well in a GUI.
This method is intended to be used only by PopupFactory sub-classes.

**Parameters:** owner

- Component mouse coordinates are relative to, may be null
**Parameters:** contents

- Contents of the Popup
**Parameters:** x

- Initial x screen coordinate
**Parameters:** y

- Initial y screen coordinate
**Parameters:** isHeavyWeightPopup

- true if Popup should be heavy weight,
otherwise popup type will be selected by popup factory.
**Returns:** Popup containing Contents
**Throws:** IllegalArgumentException

- if contents is null

---

#### Method Detail

setSharedInstance

```java
public static void setSharedInstance​(
PopupFactory
factory)
```

Sets the

PopupFactory

that will be used to obtain

Popup

s.
This will throw an

IllegalArgumentException

if

factory

is null.

**Parameters:** factory

- Shared PopupFactory
**Throws:** IllegalArgumentException

- if

factory

is null
**See Also:** getPopup(java.awt.Component, java.awt.Component, int, int)

---

#### setSharedInstance

public static void setSharedInstance​(

PopupFactory

factory)

Sets the

PopupFactory

that will be used to obtain

Popup

s.
This will throw an

IllegalArgumentException

if

factory

is null.

getSharedInstance

```java
public static
PopupFactory
getSharedInstance()
```

Returns the shared

PopupFactory

which can be used
to obtain

Popup

s.

**Returns:** Shared PopupFactory

---

#### getSharedInstance

public static

PopupFactory

getSharedInstance()

Returns the shared

PopupFactory

which can be used
to obtain

Popup

s.

getPopup

```java
public
Popup
getPopup​(
Component
owner,

Component
contents,
int x,
int y)
throws
IllegalArgumentException
```

Creates a

Popup

for the Component

owner

containing the Component

contents

.

owner

is used to determine which

Window

the new

Popup

will parent the

Component

the

Popup

creates to. A null

owner

implies there
is no valid parent.

x

and

y

specify the preferred initial location to place
the

Popup

at. Based on screen size, or other paramaters,
the

Popup

may not display at

x

and

y

.

**Parameters:** owner

- Component mouse coordinates are relative to, may be null
**Parameters:** contents

- Contents of the Popup
**Parameters:** x

- Initial x screen coordinate
**Parameters:** y

- Initial y screen coordinate
**Returns:** Popup containing Contents
**Throws:** IllegalArgumentException

- if contents is null

---

#### getPopup

public

Popup

getPopup​(

Component

owner,

Component

contents,
int x,
int y)
throws

IllegalArgumentException

Creates a

Popup

for the Component

owner

containing the Component

contents

.

owner

is used to determine which

Window

the new

Popup

will parent the

Component

the

Popup

creates to. A null

owner

implies there
is no valid parent.

x

and

y

specify the preferred initial location to place
the

Popup

at. Based on screen size, or other paramaters,
the

Popup

may not display at

x

and

y

.

getPopup

```java
protected
Popup
getPopup​(
Component
owner,

Component
contents,
int x,
int y,
boolean isHeavyWeightPopup)
throws
IllegalArgumentException
```

Creates a

Popup

for the Component

owner

containing the Component

contents

.
The window containing the component

owner

will be used as the parent window. A null

owner

implies there
is no valid parent.

x

and

y

specify the preferred
initial location to place the

Popup

at. Based on screen size,
or other parameters, the

Popup

may not display at

x

and

y

.

isHeavyWeightPopup

specifies if the

Popup

will be heavyweight. Passing

true

will force the

Popup

type to be heavyweight, otherwise

Popup

type will be selected by

Popup

factory. Lightweight

Popup

windows are more
efficient than heavyweight (native peer) windows, but lightweight
and heavyweight components do not mix well in a GUI.
This method is intended to be used only by PopupFactory sub-classes.

**Parameters:** owner

- Component mouse coordinates are relative to, may be null
**Parameters:** contents

- Contents of the Popup
**Parameters:** x

- Initial x screen coordinate
**Parameters:** y

- Initial y screen coordinate
**Parameters:** isHeavyWeightPopup

- true if Popup should be heavy weight,
otherwise popup type will be selected by popup factory.
**Returns:** Popup containing Contents
**Throws:** IllegalArgumentException

- if contents is null

---

#### getPopup

protected

Popup

getPopup​(

Component

owner,

Component

contents,
int x,
int y,
boolean isHeavyWeightPopup)
throws

IllegalArgumentException

Creates a

Popup

for the Component

owner

containing the Component

contents

.
The window containing the component

owner

will be used as the parent window. A null

owner

implies there
is no valid parent.

x

and

y

specify the preferred
initial location to place the

Popup

at. Based on screen size,
or other parameters, the

Popup

may not display at

x

and

y

.

isHeavyWeightPopup

specifies if the

Popup

will be heavyweight. Passing

true

will force the

Popup

type to be heavyweight, otherwise

Popup

type will be selected by

Popup

factory. Lightweight

Popup

windows are more
efficient than heavyweight (native peer) windows, but lightweight
and heavyweight components do not mix well in a GUI.
This method is intended to be used only by PopupFactory sub-classes.

---

