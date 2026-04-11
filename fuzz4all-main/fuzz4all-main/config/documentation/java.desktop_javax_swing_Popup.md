# Class Popup

**Source:** `java.desktop\javax\swing\Popup.html`

### Class Description

```java
public class
Popup

extends
Object
```

Popups are used to display a

Component

to the user, typically
on top of all the other

Component

s in a particular containment
hierarchy.

Popup

s have a very small life cycle. Once you
have obtained a

Popup

, and hidden it (invoked the

hide

method), you should no longer
invoke any methods on it. This allows the

PopupFactory

to cache

Popup

s for later use.

The general contract is that if you need to change the size of the

Component

, or location of the

Popup

, you should
obtain a new

Popup

.

Popup

does not descend from

Component

, rather
implementations of

Popup

are responsible for creating
and maintaining their own

Component

s to render the
requested

Component

to the user.

You typically do not explicitly create an instance of

Popup

,
instead obtain one from a

PopupFactory

.

**Since:** 1.4
**See Also:** PopupFactory

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Popup​(
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

owner

is used to determine which

Window

the new

Popup

will parent the

Component

the

Popup

creates to.
A null

owner

implies there is no valid parent.

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

**Throws:**
- IllegalArgumentException

- if contents is null

---

#### protected Popup()

Creates a

Popup

. This is provided for subclasses.

---

### Method Details

#### public void show()

Makes the

Popup

visible. If the

Popup

is
currently visible, this has no effect.

---

#### public void hide()

Hides and disposes of the

Popup

. Once a

Popup

has been disposed you should no longer invoke methods on it. A

dispose

d

Popup

may be reclaimed and later used
based on the

PopupFactory

. As such, if you invoke methods
on a

disposed

Popup

, indeterminate
behavior will result.

---

### Additional Sections

#### Class Popup

java.lang.Object

- javax.swing.Popup

javax.swing.Popup

```java
public class
Popup

extends
Object
```

Popups are used to display a

Component

to the user, typically
on top of all the other

Component

s in a particular containment
hierarchy.

Popup

s have a very small life cycle. Once you
have obtained a

Popup

, and hidden it (invoked the

hide

method), you should no longer
invoke any methods on it. This allows the

PopupFactory

to cache

Popup

s for later use.

The general contract is that if you need to change the size of the

Component

, or location of the

Popup

, you should
obtain a new

Popup

.

Popup

does not descend from

Component

, rather
implementations of

Popup

are responsible for creating
and maintaining their own

Component

s to render the
requested

Component

to the user.

You typically do not explicitly create an instance of

Popup

,
instead obtain one from a

PopupFactory

.

**Since:** 1.4
**See Also:** PopupFactory

public class

Popup

extends

Object

Popups are used to display a

Component

to the user, typically
on top of all the other

Component

s in a particular containment
hierarchy.

Popup

s have a very small life cycle. Once you
have obtained a

Popup

, and hidden it (invoked the

hide

method), you should no longer
invoke any methods on it. This allows the

PopupFactory

to cache

Popup

s for later use.

The general contract is that if you need to change the size of the

Component

, or location of the

Popup

, you should
obtain a new

Popup

.

Popup

does not descend from

Component

, rather
implementations of

Popup

are responsible for creating
and maintaining their own

Component

s to render the
requested

Component

to the user.

You typically do not explicitly create an instance of

Popup

,
instead obtain one from a

PopupFactory

.

The general contract is that if you need to change the size of the

Component

, or location of the

Popup

, you should
obtain a new

Popup

.

Popup

does not descend from

Component

, rather
implementations of

Popup

are responsible for creating
and maintaining their own

Component

s to render the
requested

Component

to the user.

You typically do not explicitly create an instance of

Popup

,
instead obtain one from a

PopupFactory

.

Popup

does not descend from

Component

, rather
implementations of

Popup

are responsible for creating
and maintaining their own

Component

s to render the
requested

Component

to the user.

You typically do not explicitly create an instance of

Popup

,
instead obtain one from a

PopupFactory

.

You typically do not explicitly create an instance of

Popup

,
instead obtain one from a

PopupFactory

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Popup

()

Creates a

Popup

.

protected

Popup

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

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

hide

()

Hides and disposes of the

Popup

.

void

show

()

Makes the

Popup

visible.

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

Modifier

Constructor

Description

protected

Popup

()

Creates a

Popup

.

protected

Popup

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

---

#### Constructor Summary

Creates a

Popup

.

Creates a

Popup

for the Component

owner

containing the Component

contents

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

hide

()

Hides and disposes of the

Popup

.

void

show

()

Makes the

Popup

visible.

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

Hides and disposes of the

Popup

.

Makes the

Popup

visible.

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

- Popup

```java
protected Popup​(
Component
owner,

Component
contents,
int x,
int y)
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

creates to.
A null

owner

implies there is no valid parent.

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
**Throws:** IllegalArgumentException

- if contents is null

- Popup

```java
protected Popup()
```

Creates a

Popup

. This is provided for subclasses.

============ METHOD DETAIL ==========

- Method Detail

- show

```java
public void show()
```

Makes the

Popup

visible. If the

Popup

is
currently visible, this has no effect.

- hide

```java
public void hide()
```

Hides and disposes of the

Popup

. Once a

Popup

has been disposed you should no longer invoke methods on it. A

dispose

d

Popup

may be reclaimed and later used
based on the

PopupFactory

. As such, if you invoke methods
on a

disposed

Popup

, indeterminate
behavior will result.

Constructor Detail

- Popup

```java
protected Popup​(
Component
owner,

Component
contents,
int x,
int y)
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

creates to.
A null

owner

implies there is no valid parent.

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
**Throws:** IllegalArgumentException

- if contents is null

- Popup

```java
protected Popup()
```

Creates a

Popup

. This is provided for subclasses.

---

#### Constructor Detail

Popup

```java
protected Popup​(
Component
owner,

Component
contents,
int x,
int y)
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

creates to.
A null

owner

implies there is no valid parent.

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
**Throws:** IllegalArgumentException

- if contents is null

---

#### Popup

protected Popup​(

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

owner

is used to determine which

Window

the new

Popup

will parent the

Component

the

Popup

creates to.
A null

owner

implies there is no valid parent.

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

Popup

```java
protected Popup()
```

Creates a

Popup

. This is provided for subclasses.

---

#### Popup

protected Popup()

Creates a

Popup

. This is provided for subclasses.

Method Detail

- show

```java
public void show()
```

Makes the

Popup

visible. If the

Popup

is
currently visible, this has no effect.

- hide

```java
public void hide()
```

Hides and disposes of the

Popup

. Once a

Popup

has been disposed you should no longer invoke methods on it. A

dispose

d

Popup

may be reclaimed and later used
based on the

PopupFactory

. As such, if you invoke methods
on a

disposed

Popup

, indeterminate
behavior will result.

---

#### Method Detail

show

```java
public void show()
```

Makes the

Popup

visible. If the

Popup

is
currently visible, this has no effect.

---

#### show

public void show()

Makes the

Popup

visible. If the

Popup

is
currently visible, this has no effect.

hide

```java
public void hide()
```

Hides and disposes of the

Popup

. Once a

Popup

has been disposed you should no longer invoke methods on it. A

dispose

d

Popup

may be reclaimed and later used
based on the

PopupFactory

. As such, if you invoke methods
on a

disposed

Popup

, indeterminate
behavior will result.

---

#### hide

public void hide()

Hides and disposes of the

Popup

. Once a

Popup

has been disposed you should no longer invoke methods on it. A

dispose

d

Popup

may be reclaimed and later used
based on the

PopupFactory

. As such, if you invoke methods
on a

disposed

Popup

, indeterminate
behavior will result.

---

