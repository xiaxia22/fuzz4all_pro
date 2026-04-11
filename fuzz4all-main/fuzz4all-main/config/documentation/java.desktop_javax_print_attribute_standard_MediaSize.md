# Class MediaSize

**Source:** `java.desktop\javax\print\attribute\standard\MediaSize.html`

### Class Description

```java
public class
MediaSize

extends
Size2DSyntax

implements
Attribute
```

Class

MediaSize

is a two-dimensional size valued printing attribute
class that indicates the dimensions of the medium in a portrait orientation,
with the

X

dimension running along the bottom edge and the

Y

dimension running along the left edge. Thus, the

Y

dimension must be
greater than or equal to the

X

dimension. Class

MediaSize

declares many standard media size values, organized into nested classes for
ISO, JIS, North American, engineering, and other media.

MediaSize

is not yet used to specify media. Its current role is as a
mapping for named media (see

MediaSizeName

). Clients
can use the mapping method

MediaSize.getMediaSizeForName(MediaSizeName)

to find the physical
dimensions of the

MediaSizeName

instances enumerated in this API.
This is useful for clients which need this information to format &
paginate printing.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

---

### Field Details

*No entries found.*

### Constructor Details

#### public MediaSize​(float x,
float y,
int units)

Construct a new media size attribute from the given floating-point
values.

**Parameters:**
- x

-

X

dimension
- y

-

Y

dimension
- units

- unit conversion factor, e.g.

Size2DSyntax.INCH

or

Size2DSyntax.MM

**Throws:**
- IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

or

x > y

---

#### public MediaSize​(int x,
int y,
int units)

Construct a new media size attribute from the given integer values.

**Parameters:**
- x

-

X

dimension
- y

-

Y

dimension
- units

- unit conversion factor, e.g.

Size2DSyntax.INCH

or

Size2DSyntax.MM

**Throws:**
- IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

or

x > y

---

#### public MediaSize​(float x,
float y,
int units,

MediaSizeName
media)

Construct a new media size attribute from the given floating-point
values.

**Parameters:**
- x

-

X

dimension
- y

-

Y

dimension
- units

- unit conversion factor, e.g.

Size2DSyntax.INCH

or

Size2DSyntax.MM
- media

- a media name to associate with this

MediaSize

**Throws:**
- IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

or

x > y

---

#### public MediaSize​(int x,
int y,
int units,

MediaSizeName
media)

Construct a new media size attribute from the given integer values.

**Parameters:**
- x

-

X

dimension
- y

-

Y

dimension
- units

- unit conversion factor, e.g.

Size2DSyntax.INCH

or

Size2DSyntax.MM
- media

- a media name to associate with this

MediaSize

**Throws:**
- IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

or

x > y

---

### Method Details

#### public
MediaSizeName
getMediaSizeName()

Get the media name, if any, for this size.

**Returns:**
- the name for this media size, or

null

if no name was
associated with this size (an anonymous size)

---

#### public static
MediaSize
getMediaSizeForName​(
MediaSizeName
media)

Get the

MediaSize

for the specified named media.

**Parameters:**
- media

- the name of the media for which the size is sought

**Returns:**
- size of the media, or

null

if this media is not
associated with any size

---

#### public static
MediaSizeName
findMedia​(float x,
float y,
int units)

The specified dimensions are used to locate a matching

MediaSize

instance from amongst all the standard

MediaSize

instances. If
there is no exact match, the closest match is used.

The

MediaSize

is in turn used to locate the

MediaSizeName

object. This method may return

null

if the closest matching

MediaSize

has no corresponding

Media

instance.

This method is useful for clients which have only dimensions and want to
find a

Media

which corresponds to the dimensions.

**Parameters:**
- x

-

X

dimension
- y

-

Y

dimension
- units

- unit conversion factor, e.g.

Size2DSyntax.INCH

or

Size2DSyntax.MM

**Returns:**
- MediaSizeName

matching these dimensions, or

null

**Throws:**
- IllegalArgumentException

- if

x <= 0

,

y <= 0

, or

units < 1

---

#### public boolean equals​(
Object
object)

Returns whether this media size attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

MediaSize

.

This media size attribute's

X

dimension is equal to

object

's

X

dimension.

This media size attribute's

Y

dimension is equal to

object

's

Y

dimension.

**Overrides:**
- equals

in class

Size2DSyntax

**Parameters:**
- object

-

Object

to compare to

**Returns:**
- true

if

object

is equivalent to this media size
attribute,

false

otherwise

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public final
Class
<? extends
Attribute
> getCategory()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

MediaSize

and any vendor-defined subclasses, the
category is class

MediaSize

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

MediaSize

and any vendor-defined subclasses, the
category name is

"media-size"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class MediaSize

java.lang.Object

- javax.print.attribute.Size2DSyntax
- - javax.print.attribute.standard.MediaSize

javax.print.attribute.Size2DSyntax

- javax.print.attribute.standard.MediaSize

javax.print.attribute.standard.MediaSize

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

```java
public class
MediaSize

extends
Size2DSyntax

implements
Attribute
```

Class

MediaSize

is a two-dimensional size valued printing attribute
class that indicates the dimensions of the medium in a portrait orientation,
with the

X

dimension running along the bottom edge and the

Y

dimension running along the left edge. Thus, the

Y

dimension must be
greater than or equal to the

X

dimension. Class

MediaSize

declares many standard media size values, organized into nested classes for
ISO, JIS, North American, engineering, and other media.

MediaSize

is not yet used to specify media. Its current role is as a
mapping for named media (see

MediaSizeName

). Clients
can use the mapping method

MediaSize.getMediaSizeForName(MediaSizeName)

to find the physical
dimensions of the

MediaSizeName

instances enumerated in this API.
This is useful for clients which need this information to format &
paginate printing.

**See Also:** Serialized Form

public class

MediaSize

extends

Size2DSyntax

implements

Attribute

Class

MediaSize

is a two-dimensional size valued printing attribute
class that indicates the dimensions of the medium in a portrait orientation,
with the

X

dimension running along the bottom edge and the

Y

dimension running along the left edge. Thus, the

Y

dimension must be
greater than or equal to the

X

dimension. Class

MediaSize

declares many standard media size values, organized into nested classes for
ISO, JIS, North American, engineering, and other media.

MediaSize

is not yet used to specify media. Its current role is as a
mapping for named media (see

MediaSizeName

). Clients
can use the mapping method

MediaSize.getMediaSizeForName(MediaSizeName)

to find the physical
dimensions of the

MediaSizeName

instances enumerated in this API.
This is useful for clients which need this information to format &
paginate printing.

MediaSize

is not yet used to specify media. Its current role is as a
mapping for named media (see

MediaSizeName

). Clients
can use the mapping method

MediaSize.getMediaSizeForName(MediaSizeName)

to find the physical
dimensions of the

MediaSizeName

instances enumerated in this API.
This is useful for clients which need this information to format &
paginate printing.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

MediaSize.Engineering

Class

MediaSize.Engineering

includes

MediaSize

values for engineering media.

static class

MediaSize.ISO

Class

MediaSize.ISO

includes

MediaSize

values
for ISO media.

static class

MediaSize.JIS

Class

MediaSize.JIS

includes

MediaSize

values
for JIS (Japanese) media.

static class

MediaSize.NA

Class

MediaSize.NA

includes

MediaSize

values
for North American media.

static class

MediaSize.Other

Class

MediaSize.Other

includes

MediaSize

values
for miscellaneous media.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.print.attribute.

Size2DSyntax

INCH

,

MM

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MediaSize

​(float x,
float y,
int units)

Construct a new media size attribute from the given floating-point
values.

MediaSize

​(float x,
float y,
int units,

MediaSizeName

media)

Construct a new media size attribute from the given floating-point
values.

MediaSize

​(int x,
int y,
int units)

Construct a new media size attribute from the given integer values.

MediaSize

​(int x,
int y,
int units,

MediaSizeName

media)

Construct a new media size attribute from the given integer values.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

object)

Returns whether this media size attribute is equivalent to the passed in
object.

static

MediaSizeName

findMedia

​(float x,
float y,
int units)

The specified dimensions are used to locate a matching

MediaSize

instance from amongst all the standard

MediaSize

instances.

Class

<? extends

Attribute

>

getCategory

()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

static

MediaSize

getMediaSizeForName

​(

MediaSizeName

media)

Get the

MediaSize

for the specified named media.

MediaSizeName

getMediaSizeName

()

Get the media name, if any, for this size.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

- Methods declared in class javax.print.attribute.

Size2DSyntax

getSize

,

getX

,

getXMicrometers

,

getY

,

getYMicrometers

,

hashCode

,

toString

,

toString

- Methods declared in class java.lang.

Object

clone

,

finalize

,

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

MediaSize.Engineering

Class

MediaSize.Engineering

includes

MediaSize

values for engineering media.

static class

MediaSize.ISO

Class

MediaSize.ISO

includes

MediaSize

values
for ISO media.

static class

MediaSize.JIS

Class

MediaSize.JIS

includes

MediaSize

values
for JIS (Japanese) media.

static class

MediaSize.NA

Class

MediaSize.NA

includes

MediaSize

values
for North American media.

static class

MediaSize.Other

Class

MediaSize.Other

includes

MediaSize

values
for miscellaneous media.

---

#### Nested Class Summary

Class

MediaSize.Engineering

includes

MediaSize

values for engineering media.

Class

MediaSize.ISO

includes

MediaSize

values
for ISO media.

Class

MediaSize.JIS

includes

MediaSize

values
for JIS (Japanese) media.

Class

MediaSize.NA

includes

MediaSize

values
for North American media.

Class

MediaSize.Other

includes

MediaSize

values
for miscellaneous media.

Field Summary

- Fields declared in class javax.print.attribute.

Size2DSyntax

INCH

,

MM

---

#### Field Summary

Fields declared in class javax.print.attribute.

Size2DSyntax

INCH

,

MM

---

#### Fields declared in class javax.print.attribute. Size2DSyntax

Constructor Summary

Constructors

Constructor

Description

MediaSize

​(float x,
float y,
int units)

Construct a new media size attribute from the given floating-point
values.

MediaSize

​(float x,
float y,
int units,

MediaSizeName

media)

Construct a new media size attribute from the given floating-point
values.

MediaSize

​(int x,
int y,
int units)

Construct a new media size attribute from the given integer values.

MediaSize

​(int x,
int y,
int units,

MediaSizeName

media)

Construct a new media size attribute from the given integer values.

---

#### Constructor Summary

Construct a new media size attribute from the given floating-point
values.

Construct a new media size attribute from the given integer values.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

object)

Returns whether this media size attribute is equivalent to the passed in
object.

static

MediaSizeName

findMedia

​(float x,
float y,
int units)

The specified dimensions are used to locate a matching

MediaSize

instance from amongst all the standard

MediaSize

instances.

Class

<? extends

Attribute

>

getCategory

()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

static

MediaSize

getMediaSizeForName

​(

MediaSizeName

media)

Get the

MediaSize

for the specified named media.

MediaSizeName

getMediaSizeName

()

Get the media name, if any, for this size.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

- Methods declared in class javax.print.attribute.

Size2DSyntax

getSize

,

getX

,

getXMicrometers

,

getY

,

getYMicrometers

,

hashCode

,

toString

,

toString

- Methods declared in class java.lang.

Object

clone

,

finalize

,

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

Returns whether this media size attribute is equivalent to the passed in
object.

The specified dimensions are used to locate a matching

MediaSize

instance from amongst all the standard

MediaSize

instances.

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

Get the

MediaSize

for the specified named media.

Get the media name, if any, for this size.

Get the name of the category of which this attribute value is an
instance.

Methods declared in class javax.print.attribute.

Size2DSyntax

getSize

,

getX

,

getXMicrometers

,

getY

,

getYMicrometers

,

hashCode

,

toString

,

toString

---

#### Methods declared in class javax.print.attribute. Size2DSyntax

Methods declared in class java.lang.

Object

clone

,

finalize

,

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MediaSize

```java
public MediaSize​(float x,
float y,
int units)
```

Construct a new media size attribute from the given floating-point
values.

**Parameters:** x

-

X

dimension
**Parameters:** y

-

Y

dimension
**Parameters:** units

- unit conversion factor, e.g.

Size2DSyntax.INCH

or

Size2DSyntax.MM
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

or

x > y

- MediaSize

```java
public MediaSize​(int x,
int y,
int units)
```

Construct a new media size attribute from the given integer values.

**Parameters:** x

-

X

dimension
**Parameters:** y

-

Y

dimension
**Parameters:** units

- unit conversion factor, e.g.

Size2DSyntax.INCH

or

Size2DSyntax.MM
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

or

x > y

- MediaSize

```java
public MediaSize​(float x,
float y,
int units,

MediaSizeName
media)
```

Construct a new media size attribute from the given floating-point
values.

**Parameters:** x

-

X

dimension
**Parameters:** y

-

Y

dimension
**Parameters:** units

- unit conversion factor, e.g.

Size2DSyntax.INCH

or

Size2DSyntax.MM
**Parameters:** media

- a media name to associate with this

MediaSize
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

or

x > y

- MediaSize

```java
public MediaSize​(int x,
int y,
int units,

MediaSizeName
media)
```

Construct a new media size attribute from the given integer values.

**Parameters:** x

-

X

dimension
**Parameters:** y

-

Y

dimension
**Parameters:** units

- unit conversion factor, e.g.

Size2DSyntax.INCH

or

Size2DSyntax.MM
**Parameters:** media

- a media name to associate with this

MediaSize
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

or

x > y

============ METHOD DETAIL ==========

- Method Detail

- getMediaSizeName

```java
public
MediaSizeName
getMediaSizeName()
```

Get the media name, if any, for this size.

**Returns:** the name for this media size, or

null

if no name was
associated with this size (an anonymous size)

- getMediaSizeForName

```java
public static
MediaSize
getMediaSizeForName​(
MediaSizeName
media)
```

Get the

MediaSize

for the specified named media.

**Parameters:** media

- the name of the media for which the size is sought
**Returns:** size of the media, or

null

if this media is not
associated with any size

- findMedia

```java
public static
MediaSizeName
findMedia​(float x,
float y,
int units)
```

The specified dimensions are used to locate a matching

MediaSize

instance from amongst all the standard

MediaSize

instances. If
there is no exact match, the closest match is used.

The

MediaSize

is in turn used to locate the

MediaSizeName

object. This method may return

null

if the closest matching

MediaSize

has no corresponding

Media

instance.

This method is useful for clients which have only dimensions and want to
find a

Media

which corresponds to the dimensions.

**Parameters:** x

-

X

dimension
**Parameters:** y

-

Y

dimension
**Parameters:** units

- unit conversion factor, e.g.

Size2DSyntax.INCH

or

Size2DSyntax.MM
**Returns:** MediaSizeName

matching these dimensions, or

null
**Throws:** IllegalArgumentException

- if

x <= 0

,

y <= 0

, or

units < 1

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this media size attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

MediaSize

.

This media size attribute's

X

dimension is equal to

object

's

X

dimension.

This media size attribute's

Y

dimension is equal to

object

's

Y

dimension.

**Overrides:** equals

in class

Size2DSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this media size
attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

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

MediaSize

and any vendor-defined subclasses, the
category is class

MediaSize

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

MediaSize

and any vendor-defined subclasses, the
category name is

"media-size"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- MediaSize

```java
public MediaSize​(float x,
float y,
int units)
```

Construct a new media size attribute from the given floating-point
values.

**Parameters:** x

-

X

dimension
**Parameters:** y

-

Y

dimension
**Parameters:** units

- unit conversion factor, e.g.

Size2DSyntax.INCH

or

Size2DSyntax.MM
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

or

x > y

- MediaSize

```java
public MediaSize​(int x,
int y,
int units)
```

Construct a new media size attribute from the given integer values.

**Parameters:** x

-

X

dimension
**Parameters:** y

-

Y

dimension
**Parameters:** units

- unit conversion factor, e.g.

Size2DSyntax.INCH

or

Size2DSyntax.MM
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

or

x > y

- MediaSize

```java
public MediaSize​(float x,
float y,
int units,

MediaSizeName
media)
```

Construct a new media size attribute from the given floating-point
values.

**Parameters:** x

-

X

dimension
**Parameters:** y

-

Y

dimension
**Parameters:** units

- unit conversion factor, e.g.

Size2DSyntax.INCH

or

Size2DSyntax.MM
**Parameters:** media

- a media name to associate with this

MediaSize
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

or

x > y

- MediaSize

```java
public MediaSize​(int x,
int y,
int units,

MediaSizeName
media)
```

Construct a new media size attribute from the given integer values.

**Parameters:** x

-

X

dimension
**Parameters:** y

-

Y

dimension
**Parameters:** units

- unit conversion factor, e.g.

Size2DSyntax.INCH

or

Size2DSyntax.MM
**Parameters:** media

- a media name to associate with this

MediaSize
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

or

x > y

---

#### Constructor Detail

MediaSize

```java
public MediaSize​(float x,
float y,
int units)
```

Construct a new media size attribute from the given floating-point
values.

**Parameters:** x

-

X

dimension
**Parameters:** y

-

Y

dimension
**Parameters:** units

- unit conversion factor, e.g.

Size2DSyntax.INCH

or

Size2DSyntax.MM
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

or

x > y

---

#### MediaSize

public MediaSize​(float x,
float y,
int units)

Construct a new media size attribute from the given floating-point
values.

MediaSize

```java
public MediaSize​(int x,
int y,
int units)
```

Construct a new media size attribute from the given integer values.

**Parameters:** x

-

X

dimension
**Parameters:** y

-

Y

dimension
**Parameters:** units

- unit conversion factor, e.g.

Size2DSyntax.INCH

or

Size2DSyntax.MM
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

or

x > y

---

#### MediaSize

public MediaSize​(int x,
int y,
int units)

Construct a new media size attribute from the given integer values.

MediaSize

```java
public MediaSize​(float x,
float y,
int units,

MediaSizeName
media)
```

Construct a new media size attribute from the given floating-point
values.

**Parameters:** x

-

X

dimension
**Parameters:** y

-

Y

dimension
**Parameters:** units

- unit conversion factor, e.g.

Size2DSyntax.INCH

or

Size2DSyntax.MM
**Parameters:** media

- a media name to associate with this

MediaSize
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

or

x > y

---

#### MediaSize

public MediaSize​(float x,
float y,
int units,

MediaSizeName

media)

Construct a new media size attribute from the given floating-point
values.

MediaSize

```java
public MediaSize​(int x,
int y,
int units,

MediaSizeName
media)
```

Construct a new media size attribute from the given integer values.

**Parameters:** x

-

X

dimension
**Parameters:** y

-

Y

dimension
**Parameters:** units

- unit conversion factor, e.g.

Size2DSyntax.INCH

or

Size2DSyntax.MM
**Parameters:** media

- a media name to associate with this

MediaSize
**Throws:** IllegalArgumentException

- if

x < 0

or

y < 0

or

units < 1

or

x > y

---

#### MediaSize

public MediaSize​(int x,
int y,
int units,

MediaSizeName

media)

Construct a new media size attribute from the given integer values.

Method Detail

- getMediaSizeName

```java
public
MediaSizeName
getMediaSizeName()
```

Get the media name, if any, for this size.

**Returns:** the name for this media size, or

null

if no name was
associated with this size (an anonymous size)

- getMediaSizeForName

```java
public static
MediaSize
getMediaSizeForName​(
MediaSizeName
media)
```

Get the

MediaSize

for the specified named media.

**Parameters:** media

- the name of the media for which the size is sought
**Returns:** size of the media, or

null

if this media is not
associated with any size

- findMedia

```java
public static
MediaSizeName
findMedia​(float x,
float y,
int units)
```

The specified dimensions are used to locate a matching

MediaSize

instance from amongst all the standard

MediaSize

instances. If
there is no exact match, the closest match is used.

The

MediaSize

is in turn used to locate the

MediaSizeName

object. This method may return

null

if the closest matching

MediaSize

has no corresponding

Media

instance.

This method is useful for clients which have only dimensions and want to
find a

Media

which corresponds to the dimensions.

**Parameters:** x

-

X

dimension
**Parameters:** y

-

Y

dimension
**Parameters:** units

- unit conversion factor, e.g.

Size2DSyntax.INCH

or

Size2DSyntax.MM
**Returns:** MediaSizeName

matching these dimensions, or

null
**Throws:** IllegalArgumentException

- if

x <= 0

,

y <= 0

, or

units < 1

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this media size attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

MediaSize

.

This media size attribute's

X

dimension is equal to

object

's

X

dimension.

This media size attribute's

Y

dimension is equal to

object

's

Y

dimension.

**Overrides:** equals

in class

Size2DSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this media size
attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

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

MediaSize

and any vendor-defined subclasses, the
category is class

MediaSize

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

MediaSize

and any vendor-defined subclasses, the
category name is

"media-size"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

---

#### Method Detail

getMediaSizeName

```java
public
MediaSizeName
getMediaSizeName()
```

Get the media name, if any, for this size.

**Returns:** the name for this media size, or

null

if no name was
associated with this size (an anonymous size)

---

#### getMediaSizeName

public

MediaSizeName

getMediaSizeName()

Get the media name, if any, for this size.

getMediaSizeForName

```java
public static
MediaSize
getMediaSizeForName​(
MediaSizeName
media)
```

Get the

MediaSize

for the specified named media.

**Parameters:** media

- the name of the media for which the size is sought
**Returns:** size of the media, or

null

if this media is not
associated with any size

---

#### getMediaSizeForName

public static

MediaSize

getMediaSizeForName​(

MediaSizeName

media)

Get the

MediaSize

for the specified named media.

findMedia

```java
public static
MediaSizeName
findMedia​(float x,
float y,
int units)
```

The specified dimensions are used to locate a matching

MediaSize

instance from amongst all the standard

MediaSize

instances. If
there is no exact match, the closest match is used.

The

MediaSize

is in turn used to locate the

MediaSizeName

object. This method may return

null

if the closest matching

MediaSize

has no corresponding

Media

instance.

This method is useful for clients which have only dimensions and want to
find a

Media

which corresponds to the dimensions.

**Parameters:** x

-

X

dimension
**Parameters:** y

-

Y

dimension
**Parameters:** units

- unit conversion factor, e.g.

Size2DSyntax.INCH

or

Size2DSyntax.MM
**Returns:** MediaSizeName

matching these dimensions, or

null
**Throws:** IllegalArgumentException

- if

x <= 0

,

y <= 0

, or

units < 1

---

#### findMedia

public static

MediaSizeName

findMedia​(float x,
float y,
int units)

The specified dimensions are used to locate a matching

MediaSize

instance from amongst all the standard

MediaSize

instances. If
there is no exact match, the closest match is used.

The

MediaSize

is in turn used to locate the

MediaSizeName

object. This method may return

null

if the closest matching

MediaSize

has no corresponding

Media

instance.

This method is useful for clients which have only dimensions and want to
find a

Media

which corresponds to the dimensions.

The

MediaSize

is in turn used to locate the

MediaSizeName

object. This method may return

null

if the closest matching

MediaSize

has no corresponding

Media

instance.

This method is useful for clients which have only dimensions and want to
find a

Media

which corresponds to the dimensions.

This method is useful for clients which have only dimensions and want to
find a

Media

which corresponds to the dimensions.

equals

```java
public boolean equals​(
Object
object)
```

Returns whether this media size attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

MediaSize

.

This media size attribute's

X

dimension is equal to

object

's

X

dimension.

This media size attribute's

Y

dimension is equal to

object

's

Y

dimension.

**Overrides:** equals

in class

Size2DSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this media size
attribute,

false

otherwise
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

object)

Returns whether this media size attribute is equivalent to the passed in
object. To be equivalent, all of the following conditions must be true:

- object

is not

null

.

object

is an instance of class

MediaSize

.

This media size attribute's

X

dimension is equal to

object

's

X

dimension.

This media size attribute's

Y

dimension is equal to

object

's

Y

dimension.

object

is not

null

.

object

is an instance of class

MediaSize

.

This media size attribute's

X

dimension is equal to

object

's

X

dimension.

This media size attribute's

Y

dimension is equal to

object

's

Y

dimension.

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

MediaSize

and any vendor-defined subclasses, the
category is class

MediaSize

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

MediaSize

and any vendor-defined subclasses, the
category is class

MediaSize

itself.

For class

MediaSize

and any vendor-defined subclasses, the
category is class

MediaSize

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

MediaSize

and any vendor-defined subclasses, the
category name is

"media-size"

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

MediaSize

and any vendor-defined subclasses, the
category name is

"media-size"

.

For class

MediaSize

and any vendor-defined subclasses, the
category name is

"media-size"

.

---

