# Class Compression

**Source:** `java.desktop\javax\print\attribute\standard\Compression.html`

### Class Description

```java
public class
Compression

extends
EnumSyntax

implements
DocAttribute
```

Class

Compression

is a printing attribute class, an enumeration, that
specifies how print data is compressed.

Compression

is an attribute
of the print data (the doc), not of the Print Job. If a

Compression

attribute is not specified for a doc, the printer assumes the doc's print
data is uncompressed (i.e., the default Compression value is always

NONE

).

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

DocAttribute

---

### Field Details

#### public static final
Compression
NONE

No compression is used.

---

#### public static final
Compression
DEFLATE

ZIP public domain inflate/deflate compression technology.

---

#### public static final
Compression
GZIP

GNU zip compression technology described in

RFC 1952

.

---

#### public static final
Compression
COMPRESS

UNIX compression technology.

---

### Constructor Details

#### protected Compression​(int value)

Construct a new compression enumeration value with the given integer
value.

**Parameters:**
- value

- Integer value

---

### Method Details

#### protected
String
[] getStringTable()

Returns the string table for class

Compression

.

**Overrides:**
- getStringTable

in class

EnumSyntax

**Returns:**
- the string table

---

#### protected
EnumSyntax
[] getEnumValueTable()

Returns the enumeration value table for class

Compression

.

**Overrides:**
- getEnumValueTable

in class

EnumSyntax

**Returns:**
- the value table

---

#### public final
Class
<? extends
Attribute
> getCategory()

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

For class

Compression

and any vendor-defined subclasses, the
category is class

Compression

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

Compression

and any vendor-defined subclasses, the
category name is

"compression"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class Compression

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.Compression

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.Compression

javax.print.attribute.standard.Compression

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

DocAttribute

```java
public class
Compression

extends
EnumSyntax

implements
DocAttribute
```

Class

Compression

is a printing attribute class, an enumeration, that
specifies how print data is compressed.

Compression

is an attribute
of the print data (the doc), not of the Print Job. If a

Compression

attribute is not specified for a doc, the printer assumes the doc's print
data is uncompressed (i.e., the default Compression value is always

NONE

).

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

**See Also:** Serialized Form

public class

Compression

extends

EnumSyntax

implements

DocAttribute

Class

Compression

is a printing attribute class, an enumeration, that
specifies how print data is compressed.

Compression

is an attribute
of the print data (the doc), not of the Print Job. If a

Compression

attribute is not specified for a doc, the printer assumes the doc's print
data is uncompressed (i.e., the default Compression value is always

NONE

).

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

Compression

COMPRESS

UNIX compression technology.

static

Compression

DEFLATE

ZIP public domain inflate/deflate compression technology.

static

Compression

GZIP

GNU zip compression technology described in

RFC 1952

.

static

Compression

NONE

No compression is used.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Compression

​(int value)

Construct a new compression enumeration value with the given integer
value.

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

protected

EnumSyntax

[]

getEnumValueTable

()

Returns the enumeration value table for class

Compression

.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

protected

String

[]

getStringTable

()

Returns the string table for class

Compression

.

- Methods declared in class javax.print.attribute.

EnumSyntax

clone

,

getOffset

,

getValue

,

hashCode

,

readResolve

,

toString

- Methods declared in class java.lang.

Object

equals

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

Fields

Modifier and Type

Field

Description

static

Compression

COMPRESS

UNIX compression technology.

static

Compression

DEFLATE

ZIP public domain inflate/deflate compression technology.

static

Compression

GZIP

GNU zip compression technology described in

RFC 1952

.

static

Compression

NONE

No compression is used.

---

#### Field Summary

UNIX compression technology.

ZIP public domain inflate/deflate compression technology.

GNU zip compression technology described in

RFC 1952

.

No compression is used.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Compression

​(int value)

Construct a new compression enumeration value with the given integer
value.

---

#### Constructor Summary

Construct a new compression enumeration value with the given integer
value.

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

protected

EnumSyntax

[]

getEnumValueTable

()

Returns the enumeration value table for class

Compression

.

String

getName

()

Get the name of the category of which this attribute value is an
instance.

protected

String

[]

getStringTable

()

Returns the string table for class

Compression

.

- Methods declared in class javax.print.attribute.

EnumSyntax

clone

,

getOffset

,

getValue

,

hashCode

,

readResolve

,

toString

- Methods declared in class java.lang.

Object

equals

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

Get the printing attribute class which is to be used as the "category"
for this printing attribute value.

Returns the enumeration value table for class

Compression

.

Get the name of the category of which this attribute value is an
instance.

Returns the string table for class

Compression

.

Methods declared in class javax.print.attribute.

EnumSyntax

clone

,

getOffset

,

getValue

,

hashCode

,

readResolve

,

toString

---

#### Methods declared in class javax.print.attribute. EnumSyntax

Methods declared in class java.lang.

Object

equals

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

============ FIELD DETAIL ===========

- Field Detail

- NONE

```java
public static final
Compression
NONE
```

No compression is used.

- DEFLATE

```java
public static final
Compression
DEFLATE
```

ZIP public domain inflate/deflate compression technology.

- GZIP

```java
public static final
Compression
GZIP
```

GNU zip compression technology described in

RFC 1952

.

- COMPRESS

```java
public static final
Compression
COMPRESS
```

UNIX compression technology.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Compression

```java
protected Compression​(int value)
```

Construct a new compression enumeration value with the given integer
value.

**Parameters:** value

- Integer value

============ METHOD DETAIL ==========

- Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

Compression

.

**Overrides:** getStringTable

in class

EnumSyntax
**Returns:** the string table

- getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

Compression

.

**Overrides:** getEnumValueTable

in class

EnumSyntax
**Returns:** the value table

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

Compression

and any vendor-defined subclasses, the
category is class

Compression

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

Compression

and any vendor-defined subclasses, the
category name is

"compression"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Field Detail

- NONE

```java
public static final
Compression
NONE
```

No compression is used.

- DEFLATE

```java
public static final
Compression
DEFLATE
```

ZIP public domain inflate/deflate compression technology.

- GZIP

```java
public static final
Compression
GZIP
```

GNU zip compression technology described in

RFC 1952

.

- COMPRESS

```java
public static final
Compression
COMPRESS
```

UNIX compression technology.

---

#### Field Detail

NONE

```java
public static final
Compression
NONE
```

No compression is used.

---

#### NONE

public static final

Compression

NONE

No compression is used.

DEFLATE

```java
public static final
Compression
DEFLATE
```

ZIP public domain inflate/deflate compression technology.

---

#### DEFLATE

public static final

Compression

DEFLATE

ZIP public domain inflate/deflate compression technology.

GZIP

```java
public static final
Compression
GZIP
```

GNU zip compression technology described in

RFC 1952

.

---

#### GZIP

public static final

Compression

GZIP

GNU zip compression technology described in

RFC 1952

.

COMPRESS

```java
public static final
Compression
COMPRESS
```

UNIX compression technology.

---

#### COMPRESS

public static final

Compression

COMPRESS

UNIX compression technology.

Constructor Detail

- Compression

```java
protected Compression​(int value)
```

Construct a new compression enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

Compression

```java
protected Compression​(int value)
```

Construct a new compression enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### Compression

protected Compression​(int value)

Construct a new compression enumeration value with the given integer
value.

Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

Compression

.

**Overrides:** getStringTable

in class

EnumSyntax
**Returns:** the string table

- getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

Compression

.

**Overrides:** getEnumValueTable

in class

EnumSyntax
**Returns:** the value table

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

Compression

and any vendor-defined subclasses, the
category is class

Compression

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

Compression

and any vendor-defined subclasses, the
category name is

"compression"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

---

#### Method Detail

getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

Compression

.

**Overrides:** getStringTable

in class

EnumSyntax
**Returns:** the string table

---

#### getStringTable

protected

String

[] getStringTable()

Returns the string table for class

Compression

.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

Compression

.

**Overrides:** getEnumValueTable

in class

EnumSyntax
**Returns:** the value table

---

#### getEnumValueTable

protected

EnumSyntax

[] getEnumValueTable()

Returns the enumeration value table for class

Compression

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

Compression

and any vendor-defined subclasses, the
category is class

Compression

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

Compression

and any vendor-defined subclasses, the
category is class

Compression

itself.

For class

Compression

and any vendor-defined subclasses, the
category is class

Compression

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

Compression

and any vendor-defined subclasses, the
category name is

"compression"

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

Compression

and any vendor-defined subclasses, the
category name is

"compression"

.

For class

Compression

and any vendor-defined subclasses, the
category name is

"compression"

.

---

