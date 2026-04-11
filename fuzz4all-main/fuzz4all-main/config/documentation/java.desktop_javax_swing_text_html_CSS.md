# Class CSS

**Source:** `java.desktop\javax\swing\text\html\CSS.html`

### Class Description

```java
public class
CSS

extends
Object

implements
Serializable
```

Defines a set of

CSS attributes

as a typesafe enumeration. The HTML View implementations use
CSS attributes to determine how they will render. This also defines
methods to map between CSS/HTML/StyleConstants. Any shorthand
properties, such as font, are mapped to the intrinsic properties.

The following describes the CSS properties that are supported by the
rendering engine:

- font-family

font-style

font-size (supports relative units)

font-weight

font

color

background-color (with the exception of transparent)

background-image

background-repeat

background-position

background

text-decoration (with the exception of blink and overline)

vertical-align (only sup and super)

text-align (justify is treated as center)

margin-top

margin-right

margin-bottom

margin-left

margin

padding-top

padding-right

padding-bottom

padding-left

padding

border-top-style

border-right-style

border-bottom-style

border-left-style

border-style (only supports inset, outset and none)

border-top-color

border-right-color

border-bottom-color

border-left-color

border-color

list-style-image

list-style-type

list-style-position

The following are modeled, but currently not rendered.

- font-variant

background-attachment (background always treated as scroll)

word-spacing

letter-spacing

text-indent

text-transform

line-height

border-top-width (this is used to indicate if a border should be used)

border-right-width

border-bottom-width

border-left-width

border-width

border-top

border-right

border-bottom

border-left

border

width

height

float

clear

display

white-space

list-style

Note: for the time being we do not fully support relative units,
unless noted, so that
p { margin-top: 10% } will be treated as if no margin-top was specified.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public CSS()

Constructs a CSS object.

---

### Method Details

#### public static
CSS.Attribute
[] getAllAttributeKeys()

Return the set of all possible CSS attribute keys.

**Returns:**
- the set of all possible CSS attribute keys

---

#### public static final
CSS.Attribute
getAttribute​(
String
name)

Translates a string to a

CSS.Attribute

object.
This will return

null

if there is no attribute
by the given name.

**Parameters:**
- name

- the name of the CSS attribute to fetch the
typesafe enumeration for

**Returns:**
- the

CSS.Attribute

object,
or

null

if the string
doesn't represent a valid attribute key

---

### Additional Sections

#### Class CSS

java.lang.Object

- javax.swing.text.html.CSS

javax.swing.text.html.CSS

**All Implemented Interfaces:** Serializable

```java
public class
CSS

extends
Object

implements
Serializable
```

Defines a set of

CSS attributes

as a typesafe enumeration. The HTML View implementations use
CSS attributes to determine how they will render. This also defines
methods to map between CSS/HTML/StyleConstants. Any shorthand
properties, such as font, are mapped to the intrinsic properties.

The following describes the CSS properties that are supported by the
rendering engine:

- font-family

font-style

font-size (supports relative units)

font-weight

font

color

background-color (with the exception of transparent)

background-image

background-repeat

background-position

background

text-decoration (with the exception of blink and overline)

vertical-align (only sup and super)

text-align (justify is treated as center)

margin-top

margin-right

margin-bottom

margin-left

margin

padding-top

padding-right

padding-bottom

padding-left

padding

border-top-style

border-right-style

border-bottom-style

border-left-style

border-style (only supports inset, outset and none)

border-top-color

border-right-color

border-bottom-color

border-left-color

border-color

list-style-image

list-style-type

list-style-position

The following are modeled, but currently not rendered.

- font-variant

background-attachment (background always treated as scroll)

word-spacing

letter-spacing

text-indent

text-transform

line-height

border-top-width (this is used to indicate if a border should be used)

border-right-width

border-bottom-width

border-left-width

border-width

border-top

border-right

border-bottom

border-left

border

width

height

float

clear

display

white-space

list-style

Note: for the time being we do not fully support relative units,
unless noted, so that
p { margin-top: 10% } will be treated as if no margin-top was specified.

**See Also:** StyleSheet

,

Serialized Form

public class

CSS

extends

Object

implements

Serializable

Defines a set of

CSS attributes

as a typesafe enumeration. The HTML View implementations use
CSS attributes to determine how they will render. This also defines
methods to map between CSS/HTML/StyleConstants. Any shorthand
properties, such as font, are mapped to the intrinsic properties.

The following describes the CSS properties that are supported by the
rendering engine:

- font-family

font-style

font-size (supports relative units)

font-weight

font

color

background-color (with the exception of transparent)

background-image

background-repeat

background-position

background

text-decoration (with the exception of blink and overline)

vertical-align (only sup and super)

text-align (justify is treated as center)

margin-top

margin-right

margin-bottom

margin-left

margin

padding-top

padding-right

padding-bottom

padding-left

padding

border-top-style

border-right-style

border-bottom-style

border-left-style

border-style (only supports inset, outset and none)

border-top-color

border-right-color

border-bottom-color

border-left-color

border-color

list-style-image

list-style-type

list-style-position

The following are modeled, but currently not rendered.

- font-variant

background-attachment (background always treated as scroll)

word-spacing

letter-spacing

text-indent

text-transform

line-height

border-top-width (this is used to indicate if a border should be used)

border-right-width

border-bottom-width

border-left-width

border-width

border-top

border-right

border-bottom

border-left

border

width

height

float

clear

display

white-space

list-style

Note: for the time being we do not fully support relative units,
unless noted, so that
p { margin-top: 10% } will be treated as if no margin-top was specified.

The following describes the CSS properties that are supported by the
rendering engine:

- font-family

font-style

font-size (supports relative units)

font-weight

font

color

background-color (with the exception of transparent)

background-image

background-repeat

background-position

background

text-decoration (with the exception of blink and overline)

vertical-align (only sup and super)

text-align (justify is treated as center)

margin-top

margin-right

margin-bottom

margin-left

margin

padding-top

padding-right

padding-bottom

padding-left

padding

border-top-style

border-right-style

border-bottom-style

border-left-style

border-style (only supports inset, outset and none)

border-top-color

border-right-color

border-bottom-color

border-left-color

border-color

list-style-image

list-style-type

list-style-position

The following are modeled, but currently not rendered.

- font-variant

background-attachment (background always treated as scroll)

word-spacing

letter-spacing

text-indent

text-transform

line-height

border-top-width (this is used to indicate if a border should be used)

border-right-width

border-bottom-width

border-left-width

border-width

border-top

border-right

border-bottom

border-left

border

width

height

float

clear

display

white-space

list-style

Note: for the time being we do not fully support relative units,
unless noted, so that
p { margin-top: 10% } will be treated as if no margin-top was specified.

font-family

font-style

font-size (supports relative units)

font-weight

font

color

background-color (with the exception of transparent)

background-image

background-repeat

background-position

background

text-decoration (with the exception of blink and overline)

vertical-align (only sup and super)

text-align (justify is treated as center)

margin-top

margin-right

margin-bottom

margin-left

margin

padding-top

padding-right

padding-bottom

padding-left

padding

border-top-style

border-right-style

border-bottom-style

border-left-style

border-style (only supports inset, outset and none)

border-top-color

border-right-color

border-bottom-color

border-left-color

border-color

list-style-image

list-style-type

list-style-position

font-variant

background-attachment (background always treated as scroll)

word-spacing

letter-spacing

text-indent

text-transform

line-height

border-top-width (this is used to indicate if a border should be used)

border-right-width

border-bottom-width

border-left-width

border-width

border-top

border-right

border-bottom

border-left

border

width

height

float

clear

display

white-space

list-style

Note: for the time being we do not fully support relative units,
unless noted, so that
p { margin-top: 10% } will be treated as if no margin-top was specified.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

CSS.Attribute

Definitions to be used as a key on AttributeSet's
that might hold CSS attributes.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CSS

()

Constructs a CSS object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

CSS.Attribute

[]

getAllAttributeKeys

()

Return the set of all possible CSS attribute keys.

static

CSS.Attribute

getAttribute

​(

String

name)

Translates a string to a

CSS.Attribute

object.

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

CSS.Attribute

Definitions to be used as a key on AttributeSet's
that might hold CSS attributes.

---

#### Nested Class Summary

Definitions to be used as a key on AttributeSet's
that might hold CSS attributes.

Constructor Summary

Constructors

Constructor

Description

CSS

()

Constructs a CSS object.

---

#### Constructor Summary

Constructs a CSS object.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

CSS.Attribute

[]

getAllAttributeKeys

()

Return the set of all possible CSS attribute keys.

static

CSS.Attribute

getAttribute

​(

String

name)

Translates a string to a

CSS.Attribute

object.

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

Return the set of all possible CSS attribute keys.

Translates a string to a

CSS.Attribute

object.

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

- CSS

```java
public CSS()
```

Constructs a CSS object.

============ METHOD DETAIL ==========

- Method Detail

- getAllAttributeKeys

```java
public static
CSS.Attribute
[] getAllAttributeKeys()
```

Return the set of all possible CSS attribute keys.

**Returns:** the set of all possible CSS attribute keys

- getAttribute

```java
public static final
CSS.Attribute
getAttribute​(
String
name)
```

Translates a string to a

CSS.Attribute

object.
This will return

null

if there is no attribute
by the given name.

**Parameters:** name

- the name of the CSS attribute to fetch the
typesafe enumeration for
**Returns:** the

CSS.Attribute

object,
or

null

if the string
doesn't represent a valid attribute key

Constructor Detail

- CSS

```java
public CSS()
```

Constructs a CSS object.

---

#### Constructor Detail

CSS

```java
public CSS()
```

Constructs a CSS object.

---

#### CSS

public CSS()

Constructs a CSS object.

Method Detail

- getAllAttributeKeys

```java
public static
CSS.Attribute
[] getAllAttributeKeys()
```

Return the set of all possible CSS attribute keys.

**Returns:** the set of all possible CSS attribute keys

- getAttribute

```java
public static final
CSS.Attribute
getAttribute​(
String
name)
```

Translates a string to a

CSS.Attribute

object.
This will return

null

if there is no attribute
by the given name.

**Parameters:** name

- the name of the CSS attribute to fetch the
typesafe enumeration for
**Returns:** the

CSS.Attribute

object,
or

null

if the string
doesn't represent a valid attribute key

---

#### Method Detail

getAllAttributeKeys

```java
public static
CSS.Attribute
[] getAllAttributeKeys()
```

Return the set of all possible CSS attribute keys.

**Returns:** the set of all possible CSS attribute keys

---

#### getAllAttributeKeys

public static

CSS.Attribute

[] getAllAttributeKeys()

Return the set of all possible CSS attribute keys.

getAttribute

```java
public static final
CSS.Attribute
getAttribute​(
String
name)
```

Translates a string to a

CSS.Attribute

object.
This will return

null

if there is no attribute
by the given name.

**Parameters:** name

- the name of the CSS attribute to fetch the
typesafe enumeration for
**Returns:** the

CSS.Attribute

object,
or

null

if the string
doesn't represent a valid attribute key

---

#### getAttribute

public static final

CSS.Attribute

getAttribute​(

String

name)

Translates a string to a

CSS.Attribute

object.
This will return

null

if there is no attribute
by the given name.

---

