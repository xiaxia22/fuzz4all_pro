# Class Severity

**Source:** `java.desktop\javax\print\attribute\standard\Severity.html`

### Class Description

```java
public final class
Severity

extends
EnumSyntax

implements
Attribute
```

Class

Severity

is a printing attribute class, an enumeration, that
denotes the severity of a

PrinterStateReason

attribute.

Instances of

Severity

do not appear in a Print Service's attribute
set directly. Rather, a

PrinterStateReasons

attribute appears in the Print Service's attribute set.
The

PrinterStateReasons

attribute contains zero,
one, or more than one

PrinterStateReason

objects
which pertain to the Print Service's status, and each

PrinterStateReason

object is associated with a
Severity level of

REPORT

(least severe),

WARNING

, or

ERROR

(most severe). The printer adds a

PrinterStateReason

object to the Print Service's

PrinterStateReasons

attribute when the
corresponding condition becomes true of the printer, and the printer removes
the

PrinterStateReason

object again when the
corresponding condition becomes false, regardless of whether the Print
Service's overall

PrinterState

also changed.

IPP Compatibility:

Severity.toString()

returns either "error",
"warning", or "report". The string values returned by each individual

PrinterStateReason

and associated

Severity

object's

toString()

methods, concatenated together with a hyphen (

"-"

)
in between, gives the IPP keyword value for a

PrinterStateReasons

.
The category name returned by

getName()

gives the IPP attribute name.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

---

### Field Details

#### public static final
Severity
REPORT

Indicates that the

PrinterStateReason

is a
"report" (least severe). An implementation may choose to omit some or all
reports. Some reports specify finer granularity about the printer state;
others serve as a precursor to a warning. A report must contain nothing
that could affect the printed output.

---

#### public static final
Severity
WARNING

Indicates that the

PrinterStateReason

is a
"warning." An implementation may choose to omit some or all warnings.
Warnings serve as a precursor to an error. A warning must contain nothing
that prevents a job from completing, though in some cases the output may
be of lower quality.

---

#### public static final
Severity
ERROR

Indicates that the

PrinterStateReason

is an
"error" (most severe). An implementation must include all errors. If this
attribute contains one or more errors, the printer's

PrinterState

must be

STOPPED

.

---

### Constructor Details

#### protected Severity​(int value)

Construct a new severity enumeration value with the given integer value.

**Parameters:**
- value

- Integer value

---

### Method Details

#### protected
String
[] getStringTable()

Returns the string table for class

Severity

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

Severity

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

Severity

, the category is class

Severity

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

Severity

, the category name is

"severity"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class Severity

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.Severity

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.Severity

javax.print.attribute.standard.Severity

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

```java
public final class
Severity

extends
EnumSyntax

implements
Attribute
```

Class

Severity

is a printing attribute class, an enumeration, that
denotes the severity of a

PrinterStateReason

attribute.

Instances of

Severity

do not appear in a Print Service's attribute
set directly. Rather, a

PrinterStateReasons

attribute appears in the Print Service's attribute set.
The

PrinterStateReasons

attribute contains zero,
one, or more than one

PrinterStateReason

objects
which pertain to the Print Service's status, and each

PrinterStateReason

object is associated with a
Severity level of

REPORT

(least severe),

WARNING

, or

ERROR

(most severe). The printer adds a

PrinterStateReason

object to the Print Service's

PrinterStateReasons

attribute when the
corresponding condition becomes true of the printer, and the printer removes
the

PrinterStateReason

object again when the
corresponding condition becomes false, regardless of whether the Print
Service's overall

PrinterState

also changed.

IPP Compatibility:

Severity.toString()

returns either "error",
"warning", or "report". The string values returned by each individual

PrinterStateReason

and associated

Severity

object's

toString()

methods, concatenated together with a hyphen (

"-"

)
in between, gives the IPP keyword value for a

PrinterStateReasons

.
The category name returned by

getName()

gives the IPP attribute name.

**See Also:** Serialized Form

public final class

Severity

extends

EnumSyntax

implements

Attribute

Class

Severity

is a printing attribute class, an enumeration, that
denotes the severity of a

PrinterStateReason

attribute.

Instances of

Severity

do not appear in a Print Service's attribute
set directly. Rather, a

PrinterStateReasons

attribute appears in the Print Service's attribute set.
The

PrinterStateReasons

attribute contains zero,
one, or more than one

PrinterStateReason

objects
which pertain to the Print Service's status, and each

PrinterStateReason

object is associated with a
Severity level of

REPORT

(least severe),

WARNING

, or

ERROR

(most severe). The printer adds a

PrinterStateReason

object to the Print Service's

PrinterStateReasons

attribute when the
corresponding condition becomes true of the printer, and the printer removes
the

PrinterStateReason

object again when the
corresponding condition becomes false, regardless of whether the Print
Service's overall

PrinterState

also changed.

IPP Compatibility:

Severity.toString()

returns either "error",
"warning", or "report". The string values returned by each individual

PrinterStateReason

and associated

Severity

object's

toString()

methods, concatenated together with a hyphen (

"-"

)
in between, gives the IPP keyword value for a

PrinterStateReasons

.
The category name returned by

getName()

gives the IPP attribute name.

Instances of

Severity

do not appear in a Print Service's attribute
set directly. Rather, a

PrinterStateReasons

attribute appears in the Print Service's attribute set.
The

PrinterStateReasons

attribute contains zero,
one, or more than one

PrinterStateReason

objects
which pertain to the Print Service's status, and each

PrinterStateReason

object is associated with a
Severity level of

REPORT

(least severe),

WARNING

, or

ERROR

(most severe). The printer adds a

PrinterStateReason

object to the Print Service's

PrinterStateReasons

attribute when the
corresponding condition becomes true of the printer, and the printer removes
the

PrinterStateReason

object again when the
corresponding condition becomes false, regardless of whether the Print
Service's overall

PrinterState

also changed.

IPP Compatibility:

Severity.toString()

returns either "error",
"warning", or "report". The string values returned by each individual

PrinterStateReason

and associated

Severity

object's

toString()

methods, concatenated together with a hyphen (

"-"

)
in between, gives the IPP keyword value for a

PrinterStateReasons

.
The category name returned by

getName()

gives the IPP attribute name.

IPP Compatibility:

Severity.toString()

returns either "error",
"warning", or "report". The string values returned by each individual

PrinterStateReason

and associated

Severity

object's

toString()

methods, concatenated together with a hyphen (

"-"

)
in between, gives the IPP keyword value for a

PrinterStateReasons

.
The category name returned by

getName()

gives the IPP attribute name.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

Severity

ERROR

Indicates that the

PrinterStateReason

is an
"error" (most severe).

static

Severity

REPORT

Indicates that the

PrinterStateReason

is a
"report" (least severe).

static

Severity

WARNING

Indicates that the

PrinterStateReason

is a
"warning."

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Severity

​(int value)

Construct a new severity enumeration value with the given integer value.

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

Severity

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

Severity

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

Severity

ERROR

Indicates that the

PrinterStateReason

is an
"error" (most severe).

static

Severity

REPORT

Indicates that the

PrinterStateReason

is a
"report" (least severe).

static

Severity

WARNING

Indicates that the

PrinterStateReason

is a
"warning."

---

#### Field Summary

Indicates that the

PrinterStateReason

is an
"error" (most severe).

Indicates that the

PrinterStateReason

is a
"report" (least severe).

Indicates that the

PrinterStateReason

is a
"warning."

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Severity

​(int value)

Construct a new severity enumeration value with the given integer value.

---

#### Constructor Summary

Construct a new severity enumeration value with the given integer value.

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

Severity

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

Severity

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

Severity

.

Get the name of the category of which this attribute value is an
instance.

Returns the string table for class

Severity

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

- REPORT

```java
public static final
Severity
REPORT
```

Indicates that the

PrinterStateReason

is a
"report" (least severe). An implementation may choose to omit some or all
reports. Some reports specify finer granularity about the printer state;
others serve as a precursor to a warning. A report must contain nothing
that could affect the printed output.

- WARNING

```java
public static final
Severity
WARNING
```

Indicates that the

PrinterStateReason

is a
"warning." An implementation may choose to omit some or all warnings.
Warnings serve as a precursor to an error. A warning must contain nothing
that prevents a job from completing, though in some cases the output may
be of lower quality.

- ERROR

```java
public static final
Severity
ERROR
```

Indicates that the

PrinterStateReason

is an
"error" (most severe). An implementation must include all errors. If this
attribute contains one or more errors, the printer's

PrinterState

must be

STOPPED

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Severity

```java
protected Severity​(int value)
```

Construct a new severity enumeration value with the given integer value.

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

Severity

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

Severity

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

Severity

, the category is class

Severity

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

Severity

, the category name is

"severity"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Field Detail

- REPORT

```java
public static final
Severity
REPORT
```

Indicates that the

PrinterStateReason

is a
"report" (least severe). An implementation may choose to omit some or all
reports. Some reports specify finer granularity about the printer state;
others serve as a precursor to a warning. A report must contain nothing
that could affect the printed output.

- WARNING

```java
public static final
Severity
WARNING
```

Indicates that the

PrinterStateReason

is a
"warning." An implementation may choose to omit some or all warnings.
Warnings serve as a precursor to an error. A warning must contain nothing
that prevents a job from completing, though in some cases the output may
be of lower quality.

- ERROR

```java
public static final
Severity
ERROR
```

Indicates that the

PrinterStateReason

is an
"error" (most severe). An implementation must include all errors. If this
attribute contains one or more errors, the printer's

PrinterState

must be

STOPPED

.

---

#### Field Detail

REPORT

```java
public static final
Severity
REPORT
```

Indicates that the

PrinterStateReason

is a
"report" (least severe). An implementation may choose to omit some or all
reports. Some reports specify finer granularity about the printer state;
others serve as a precursor to a warning. A report must contain nothing
that could affect the printed output.

---

#### REPORT

public static final

Severity

REPORT

Indicates that the

PrinterStateReason

is a
"report" (least severe). An implementation may choose to omit some or all
reports. Some reports specify finer granularity about the printer state;
others serve as a precursor to a warning. A report must contain nothing
that could affect the printed output.

WARNING

```java
public static final
Severity
WARNING
```

Indicates that the

PrinterStateReason

is a
"warning." An implementation may choose to omit some or all warnings.
Warnings serve as a precursor to an error. A warning must contain nothing
that prevents a job from completing, though in some cases the output may
be of lower quality.

---

#### WARNING

public static final

Severity

WARNING

Indicates that the

PrinterStateReason

is a
"warning." An implementation may choose to omit some or all warnings.
Warnings serve as a precursor to an error. A warning must contain nothing
that prevents a job from completing, though in some cases the output may
be of lower quality.

ERROR

```java
public static final
Severity
ERROR
```

Indicates that the

PrinterStateReason

is an
"error" (most severe). An implementation must include all errors. If this
attribute contains one or more errors, the printer's

PrinterState

must be

STOPPED

.

---

#### ERROR

public static final

Severity

ERROR

Indicates that the

PrinterStateReason

is an
"error" (most severe). An implementation must include all errors. If this
attribute contains one or more errors, the printer's

PrinterState

must be

STOPPED

.

Constructor Detail

- Severity

```java
protected Severity​(int value)
```

Construct a new severity enumeration value with the given integer value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

Severity

```java
protected Severity​(int value)
```

Construct a new severity enumeration value with the given integer value.

**Parameters:** value

- Integer value

---

#### Severity

protected Severity​(int value)

Construct a new severity enumeration value with the given integer value.

Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

Severity

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

Severity

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

Severity

, the category is class

Severity

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

Severity

, the category name is

"severity"

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

Severity

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

Severity

.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

Severity

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

Severity

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

Severity

, the category is class

Severity

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

Severity

, the category is class

Severity

itself.

For class

Severity

, the category is class

Severity

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

Severity

, the category name is

"severity"

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

Severity

, the category name is

"severity"

.

For class

Severity

, the category name is

"severity"

.

---

