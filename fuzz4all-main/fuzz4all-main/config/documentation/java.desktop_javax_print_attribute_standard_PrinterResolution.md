# Class PrinterResolution

**Source:** `java.desktop\javax\print\attribute\standard\PrinterResolution.html`

### Class Description

```java
public final class
PrinterResolution

extends
ResolutionSyntax

implements
DocAttribute
,
PrintRequestAttribute
,
PrintJobAttribute
```

Class

PrinterResolution

is a printing attribute class that specifies
an exact resolution supported by a printer or to be used for a print job.
This attribute assumes that printers have a small set of device resolutions
at which they can operate rather than a continuum.

PrinterResolution

is used in multiple ways:

- When a client searches looking for a printer that supports the client's
desired resolution exactly (no more, no less), the client specifies an
instance of class

PrinterResolution

indicating the exact resolution
the client wants. Only printers supporting that exact resolution will match
the search.

When a client needs to print a job using the client's desired
resolution exactly (no more, no less), the client specifies an instance of
class

PrinterResolution

as an attribute of the Print Job. This will
fail if the Print Job doesn't support that exact resolution, and

Fidelity

is set to true.

If a client wants to locate a printer supporting a resolution greater than
some required minimum, then it may be necessary to exclude this attribute
from a lookup request and to directly query the set of supported resolutions,
and specify the one that most closely meets the client's requirements. In
some cases this may be more simply achieved by specifying a

PrintQuality

attribute which often controls resolution.

IPP Compatibility:

The information needed to construct an IPP

"printer-resolution"

attribute can be obtained by calling methods on
the PrinterResolution object. The category name returned by

getName()

gives the IPP attribute name.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

DocAttribute

,

PrintJobAttribute

,

PrintRequestAttribute

---

### Field Details

*No entries found.*

### Constructor Details

#### public PrinterResolution​(int crossFeedResolution,
int feedResolution,
int units)

Construct a new printer resolution attribute from the given items.

**Parameters:**
- crossFeedResolution

- cross feed direction resolution
- feedResolution

- feed direction resolution
- units

- unit conversion factor, e.g.

ResolutionSyntax.DPI

or

ResolutionSyntax.DPCM

**Throws:**
- IllegalArgumentException

- if

crossFeedResolution < 1

or

feedResolution < 1

or

units < 1

---

### Method Details

#### public boolean equals​(
Object
object)

Returns whether this printer resolution attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

PrinterResolution

.

This attribute's cross feed direction resolution is equal to

object

's cross feed direction resolution.

This attribute's feed direction resolution is equal to

object

's feed direction resolution.

**Overrides:**
- equals

in class

ResolutionSyntax

**Parameters:**
- object

-

Object

to compare to

**Returns:**
- true

if

object

is equivalent to this printer
resolution attribute,

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

PrinterResolution

, the category is class

PrinterResolution

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

PrinterResolution

, the category name is

"printer-resolution"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class PrinterResolution

java.lang.Object

- javax.print.attribute.ResolutionSyntax
- - javax.print.attribute.standard.PrinterResolution

javax.print.attribute.ResolutionSyntax

- javax.print.attribute.standard.PrinterResolution

javax.print.attribute.standard.PrinterResolution

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

DocAttribute

,

PrintJobAttribute

,

PrintRequestAttribute

```java
public final class
PrinterResolution

extends
ResolutionSyntax

implements
DocAttribute
,
PrintRequestAttribute
,
PrintJobAttribute
```

Class

PrinterResolution

is a printing attribute class that specifies
an exact resolution supported by a printer or to be used for a print job.
This attribute assumes that printers have a small set of device resolutions
at which they can operate rather than a continuum.

PrinterResolution

is used in multiple ways:

- When a client searches looking for a printer that supports the client's
desired resolution exactly (no more, no less), the client specifies an
instance of class

PrinterResolution

indicating the exact resolution
the client wants. Only printers supporting that exact resolution will match
the search.

When a client needs to print a job using the client's desired
resolution exactly (no more, no less), the client specifies an instance of
class

PrinterResolution

as an attribute of the Print Job. This will
fail if the Print Job doesn't support that exact resolution, and

Fidelity

is set to true.

If a client wants to locate a printer supporting a resolution greater than
some required minimum, then it may be necessary to exclude this attribute
from a lookup request and to directly query the set of supported resolutions,
and specify the one that most closely meets the client's requirements. In
some cases this may be more simply achieved by specifying a

PrintQuality

attribute which often controls resolution.

IPP Compatibility:

The information needed to construct an IPP

"printer-resolution"

attribute can be obtained by calling methods on
the PrinterResolution object. The category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

PrinterResolution

extends

ResolutionSyntax

implements

DocAttribute

,

PrintRequestAttribute

,

PrintJobAttribute

Class

PrinterResolution

is a printing attribute class that specifies
an exact resolution supported by a printer or to be used for a print job.
This attribute assumes that printers have a small set of device resolutions
at which they can operate rather than a continuum.

PrinterResolution

is used in multiple ways:

- When a client searches looking for a printer that supports the client's
desired resolution exactly (no more, no less), the client specifies an
instance of class

PrinterResolution

indicating the exact resolution
the client wants. Only printers supporting that exact resolution will match
the search.

When a client needs to print a job using the client's desired
resolution exactly (no more, no less), the client specifies an instance of
class

PrinterResolution

as an attribute of the Print Job. This will
fail if the Print Job doesn't support that exact resolution, and

Fidelity

is set to true.

If a client wants to locate a printer supporting a resolution greater than
some required minimum, then it may be necessary to exclude this attribute
from a lookup request and to directly query the set of supported resolutions,
and specify the one that most closely meets the client's requirements. In
some cases this may be more simply achieved by specifying a

PrintQuality

attribute which often controls resolution.

IPP Compatibility:

The information needed to construct an IPP

"printer-resolution"

attribute can be obtained by calling methods on
the PrinterResolution object. The category name returned by

getName()

gives the IPP attribute name.

PrinterResolution

is used in multiple ways:

- When a client searches looking for a printer that supports the client's
desired resolution exactly (no more, no less), the client specifies an
instance of class

PrinterResolution

indicating the exact resolution
the client wants. Only printers supporting that exact resolution will match
the search.

When a client needs to print a job using the client's desired
resolution exactly (no more, no less), the client specifies an instance of
class

PrinterResolution

as an attribute of the Print Job. This will
fail if the Print Job doesn't support that exact resolution, and

Fidelity

is set to true.

If a client wants to locate a printer supporting a resolution greater than
some required minimum, then it may be necessary to exclude this attribute
from a lookup request and to directly query the set of supported resolutions,
and specify the one that most closely meets the client's requirements. In
some cases this may be more simply achieved by specifying a

PrintQuality

attribute which often controls resolution.

IPP Compatibility:

The information needed to construct an IPP

"printer-resolution"

attribute can be obtained by calling methods on
the PrinterResolution object. The category name returned by

getName()

gives the IPP attribute name.

When a client searches looking for a printer that supports the client's
desired resolution exactly (no more, no less), the client specifies an
instance of class

PrinterResolution

indicating the exact resolution
the client wants. Only printers supporting that exact resolution will match
the search.

When a client needs to print a job using the client's desired
resolution exactly (no more, no less), the client specifies an instance of
class

PrinterResolution

as an attribute of the Print Job. This will
fail if the Print Job doesn't support that exact resolution, and

Fidelity

is set to true.

IPP Compatibility:

The information needed to construct an IPP

"printer-resolution"

attribute can be obtained by calling methods on
the PrinterResolution object. The category name returned by

getName()

gives the IPP attribute name.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.print.attribute.

ResolutionSyntax

DPCM

,

DPI

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PrinterResolution

​(int crossFeedResolution,
int feedResolution,
int units)

Construct a new printer resolution attribute from the given items.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

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

Returns whether this printer resolution attribute is equivalent to the
passed in object.

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

- Methods declared in class javax.print.attribute.

ResolutionSyntax

getCrossFeedResolution

,

getCrossFeedResolutionDphi

,

getFeedResolution

,

getFeedResolutionDphi

,

getResolution

,

hashCode

,

lessThanOrEquals

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

Field Summary

- Fields declared in class javax.print.attribute.

ResolutionSyntax

DPCM

,

DPI

---

#### Field Summary

Fields declared in class javax.print.attribute.

ResolutionSyntax

DPCM

,

DPI

---

#### Fields declared in class javax.print.attribute. ResolutionSyntax

Constructor Summary

Constructors

Constructor

Description

PrinterResolution

​(int crossFeedResolution,
int feedResolution,
int units)

Construct a new printer resolution attribute from the given items.

---

#### Constructor Summary

Construct a new printer resolution attribute from the given items.

Method Summary

All Methods

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

Returns whether this printer resolution attribute is equivalent to the
passed in object.

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

- Methods declared in class javax.print.attribute.

ResolutionSyntax

getCrossFeedResolution

,

getCrossFeedResolutionDphi

,

getFeedResolution

,

getFeedResolutionDphi

,

getResolution

,

hashCode

,

lessThanOrEquals

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

Returns whether this printer resolution attribute is equivalent to the
passed in object.

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

Get the name of the category of which this attribute value is an
instance.

Methods declared in class javax.print.attribute.

ResolutionSyntax

getCrossFeedResolution

,

getCrossFeedResolutionDphi

,

getFeedResolution

,

getFeedResolutionDphi

,

getResolution

,

hashCode

,

lessThanOrEquals

,

toString

,

toString

---

#### Methods declared in class javax.print.attribute. ResolutionSyntax

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

- PrinterResolution

```java
public PrinterResolution​(int crossFeedResolution,
int feedResolution,
int units)
```

Construct a new printer resolution attribute from the given items.

**Parameters:** crossFeedResolution

- cross feed direction resolution
**Parameters:** feedResolution

- feed direction resolution
**Parameters:** units

- unit conversion factor, e.g.

ResolutionSyntax.DPI

or

ResolutionSyntax.DPCM
**Throws:** IllegalArgumentException

- if

crossFeedResolution < 1

or

feedResolution < 1

or

units < 1

============ METHOD DETAIL ==========

- Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this printer resolution attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

PrinterResolution

.

This attribute's cross feed direction resolution is equal to

object

's cross feed direction resolution.

This attribute's feed direction resolution is equal to

object

's feed direction resolution.

**Overrides:** equals

in class

ResolutionSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this printer
resolution attribute,

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

PrinterResolution

, the category is class

PrinterResolution

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

PrinterResolution

, the category name is

"printer-resolution"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Constructor Detail

- PrinterResolution

```java
public PrinterResolution​(int crossFeedResolution,
int feedResolution,
int units)
```

Construct a new printer resolution attribute from the given items.

**Parameters:** crossFeedResolution

- cross feed direction resolution
**Parameters:** feedResolution

- feed direction resolution
**Parameters:** units

- unit conversion factor, e.g.

ResolutionSyntax.DPI

or

ResolutionSyntax.DPCM
**Throws:** IllegalArgumentException

- if

crossFeedResolution < 1

or

feedResolution < 1

or

units < 1

---

#### Constructor Detail

PrinterResolution

```java
public PrinterResolution​(int crossFeedResolution,
int feedResolution,
int units)
```

Construct a new printer resolution attribute from the given items.

**Parameters:** crossFeedResolution

- cross feed direction resolution
**Parameters:** feedResolution

- feed direction resolution
**Parameters:** units

- unit conversion factor, e.g.

ResolutionSyntax.DPI

or

ResolutionSyntax.DPCM
**Throws:** IllegalArgumentException

- if

crossFeedResolution < 1

or

feedResolution < 1

or

units < 1

---

#### PrinterResolution

public PrinterResolution​(int crossFeedResolution,
int feedResolution,
int units)

Construct a new printer resolution attribute from the given items.

Method Detail

- equals

```java
public boolean equals​(
Object
object)
```

Returns whether this printer resolution attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

PrinterResolution

.

This attribute's cross feed direction resolution is equal to

object

's cross feed direction resolution.

This attribute's feed direction resolution is equal to

object

's feed direction resolution.

**Overrides:** equals

in class

ResolutionSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this printer
resolution attribute,

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

PrinterResolution

, the category is class

PrinterResolution

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

PrinterResolution

, the category name is

"printer-resolution"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

---

#### Method Detail

equals

```java
public boolean equals​(
Object
object)
```

Returns whether this printer resolution attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

PrinterResolution

.

This attribute's cross feed direction resolution is equal to

object

's cross feed direction resolution.

This attribute's feed direction resolution is equal to

object

's feed direction resolution.

**Overrides:** equals

in class

ResolutionSyntax
**Parameters:** object

-

Object

to compare to
**Returns:** true

if

object

is equivalent to this printer
resolution attribute,

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

Returns whether this printer resolution attribute is equivalent to the
passed in object. To be equivalent, all of the following conditions must
be true:

- object

is not

null

.

object

is an instance of class

PrinterResolution

.

This attribute's cross feed direction resolution is equal to

object

's cross feed direction resolution.

This attribute's feed direction resolution is equal to

object

's feed direction resolution.

object

is not

null

.

object

is an instance of class

PrinterResolution

.

This attribute's cross feed direction resolution is equal to

object

's cross feed direction resolution.

This attribute's feed direction resolution is equal to

object

's feed direction resolution.

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

PrinterResolution

, the category is class

PrinterResolution

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

PrinterResolution

, the category is class

PrinterResolution

itself.

For class

PrinterResolution

, the category is class

PrinterResolution

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

PrinterResolution

, the category name is

"printer-resolution"

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

PrinterResolution

, the category name is

"printer-resolution"

.

For class

PrinterResolution

, the category name is

"printer-resolution"

.

---

