# Class DialogOwner

**Source:** `java.desktop\javax\print\attribute\standard\DialogOwner.html`

### Class Description

```java
public final class
DialogOwner

extends
Object

implements
PrintRequestAttribute
```

An attribute class used to support requesting a print or page setup dialog
be kept displayed on top of all windows or some specific window.

Constructed without any arguments it will request that a print or page
setup dialog be configured as if the application directly was to specify

java.awt.Window.setAlwaysOnTop(true)

, subject to permission checks.

Constructed with a

Window

parameter, it requests that
the dialog be owned by the specified window.

**All Implemented Interfaces:** Serializable

,

Attribute

,

PrintRequestAttribute

---

### Field Details

*No entries found.*

### Constructor Details

#### public DialogOwner()

Constructs an instance which can be used to request

java.awt.Window.setAlwaysOnTop(true)

behaviour.
This should be used where there is no application preferred owner window.
Whether this has any effect depends on if always on top is supported
for this platform and the particular dialog to be displayed.

---

#### public DialogOwner​(
Window
owner)

Constructs an instance which can be used to request that the
specified

Window

be the owner of the dialog.

**Parameters:**
- owner

- window.

---

### Method Details

#### public
Window
getOwner()

Returns a

Window owner

, if one was specified,
otherwise

null

.

**Returns:**
- an owner window.

---

#### public final
Class
<? extends
Attribute
> getCategory()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

DialogOwner

, the category is class

DialogOwner

itself.

**Specified by:**
- getCategory

in interface

Attribute

**Returns:**
- printing attribute class (category), an instance of class

java.lang.Class

---

#### public final
String
getName()

Get the name of the category of which this attribute value is an
instance.

For class

DialogOwner

, the category name is

"dialog-owner"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class DialogOwner

java.lang.Object

- javax.print.attribute.standard.DialogOwner

javax.print.attribute.standard.DialogOwner

**All Implemented Interfaces:** Serializable

,

Attribute

,

PrintRequestAttribute

```java
public final class
DialogOwner

extends
Object

implements
PrintRequestAttribute
```

An attribute class used to support requesting a print or page setup dialog
be kept displayed on top of all windows or some specific window.

Constructed without any arguments it will request that a print or page
setup dialog be configured as if the application directly was to specify

java.awt.Window.setAlwaysOnTop(true)

, subject to permission checks.

Constructed with a

Window

parameter, it requests that
the dialog be owned by the specified window.

**Since:** 11
**See Also:** Serialized Form

public final class

DialogOwner

extends

Object

implements

PrintRequestAttribute

An attribute class used to support requesting a print or page setup dialog
be kept displayed on top of all windows or some specific window.

Constructed without any arguments it will request that a print or page
setup dialog be configured as if the application directly was to specify

java.awt.Window.setAlwaysOnTop(true)

, subject to permission checks.

Constructed with a

Window

parameter, it requests that
the dialog be owned by the specified window.

Constructed without any arguments it will request that a print or page
setup dialog be configured as if the application directly was to specify

java.awt.Window.setAlwaysOnTop(true)

, subject to permission checks.

Constructed with a

Window

parameter, it requests that
the dialog be owned by the specified window.

Constructed with a

Window

parameter, it requests that
the dialog be owned by the specified window.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DialogOwner

()

Constructs an instance which can be used to request

java.awt.Window.setAlwaysOnTop(true)

behaviour.

DialogOwner

​(

Window

owner)

Constructs an instance which can be used to request that the
specified

Window

be the owner of the dialog.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<? extends

Attribute

>

getCategory

()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

Window

getOwner

()

Returns a

Window owner

, if one was specified,
otherwise

null

.

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

DialogOwner

()

Constructs an instance which can be used to request

java.awt.Window.setAlwaysOnTop(true)

behaviour.

DialogOwner

​(

Window

owner)

Constructs an instance which can be used to request that the
specified

Window

be the owner of the dialog.

---

#### Constructor Summary

Constructs an instance which can be used to request

java.awt.Window.setAlwaysOnTop(true)

behaviour.

Constructs an instance which can be used to request that the
specified

Window

be the owner of the dialog.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Class

<? extends

Attribute

>

getCategory

()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

Window

getOwner

()

Returns a

Window owner

, if one was specified,
otherwise

null

.

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

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

Get the name of the category of which this attribute value is an
instance.

Returns a

Window owner

, if one was specified,
otherwise

null

.

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

- DialogOwner

```java
public DialogOwner()
```

Constructs an instance which can be used to request

java.awt.Window.setAlwaysOnTop(true)

behaviour.
This should be used where there is no application preferred owner window.
Whether this has any effect depends on if always on top is supported
for this platform and the particular dialog to be displayed.

- DialogOwner

```java
public DialogOwner​(
Window
owner)
```

Constructs an instance which can be used to request that the
specified

Window

be the owner of the dialog.

**Parameters:** owner

- window.

============ METHOD DETAIL ==========

- Method Detail

- getOwner

```java
public
Window
getOwner()
```

Returns a

Window owner

, if one was specified,
otherwise

null

.

**Returns:** an owner window.

- getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

DialogOwner

, the category is class

DialogOwner

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

- getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

DialogOwner

, the category name is

"dialog-owner"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- DialogOwner

```java
public DialogOwner()
```

Constructs an instance which can be used to request

java.awt.Window.setAlwaysOnTop(true)

behaviour.
This should be used where there is no application preferred owner window.
Whether this has any effect depends on if always on top is supported
for this platform and the particular dialog to be displayed.

- DialogOwner

```java
public DialogOwner​(
Window
owner)
```

Constructs an instance which can be used to request that the
specified

Window

be the owner of the dialog.

**Parameters:** owner

- window.

---

#### Constructor Detail

DialogOwner

```java
public DialogOwner()
```

Constructs an instance which can be used to request

java.awt.Window.setAlwaysOnTop(true)

behaviour.
This should be used where there is no application preferred owner window.
Whether this has any effect depends on if always on top is supported
for this platform and the particular dialog to be displayed.

---

#### DialogOwner

public DialogOwner()

Constructs an instance which can be used to request

java.awt.Window.setAlwaysOnTop(true)

behaviour.
This should be used where there is no application preferred owner window.
Whether this has any effect depends on if always on top is supported
for this platform and the particular dialog to be displayed.

DialogOwner

```java
public DialogOwner​(
Window
owner)
```

Constructs an instance which can be used to request that the
specified

Window

be the owner of the dialog.

**Parameters:** owner

- window.

---

#### DialogOwner

public DialogOwner​(

Window

owner)

Constructs an instance which can be used to request that the
specified

Window

be the owner of the dialog.

Method Detail

- getOwner

```java
public
Window
getOwner()
```

Returns a

Window owner

, if one was specified,
otherwise

null

.

**Returns:** an owner window.

- getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

DialogOwner

, the category is class

DialogOwner

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

- getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

DialogOwner

, the category name is

"dialog-owner"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

---

#### Method Detail

getOwner

```java
public
Window
getOwner()
```

Returns a

Window owner

, if one was specified,
otherwise

null

.

**Returns:** an owner window.

---

#### getOwner

public

Window

getOwner()

Returns a

Window owner

, if one was specified,
otherwise

null

.

getCategory

```java
public final
Class
<? extends
Attribute
> getCategory()
```

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

DialogOwner

, the category is class

DialogOwner

itself.

**Specified by:** getCategory

in interface

Attribute
**Returns:** printing attribute class (category), an instance of class

java.lang.Class

---

#### getCategory

public final

Class

<? extends

Attribute

> getCategory()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

DialogOwner

, the category is class

DialogOwner

itself.

For class

DialogOwner

, the category is class

DialogOwner

itself.

getName

```java
public final
String
getName()
```

Get the name of the category of which this attribute value is an
instance.

For class

DialogOwner

, the category name is

"dialog-owner"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

---

#### getName

public final

String

getName()

Get the name of the category of which this attribute value is an
instance.

For class

DialogOwner

, the category name is

"dialog-owner"

.

For class

DialogOwner

, the category name is

"dialog-owner"

.

---

