# Class JobSheets

**Source:** `java.desktop\javax\print\attribute\standard\JobSheets.html`

### Class Description

```java
public class
JobSheets

extends
EnumSyntax

implements
PrintRequestAttribute
,
PrintJobAttribute
```

Class

JobSheets

is a printing attribute class, an enumeration, that
determines which job start and end sheets, if any, must be printed with a
job. Class

JobSheets

declares keywords for standard job sheets
values. Implementation- or site-defined names for a job sheets attribute may
also be created by defining a subclass of class

JobSheets

.

The effect of a

JobSheets

attribute on multidoc print jobs (jobs with
multiple documents) may be affected by the

MultipleDocumentHandling

job attribute,
depending on the meaning of the particular

JobSheets

value.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value. For a subclass, the attribute value must be localized to
give the IPP name and natural language values.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintJobAttribute

,

PrintRequestAttribute

---

### Field Details

#### public static final
JobSheets
NONE

No job sheets are printed.

---

#### public static final
JobSheets
STANDARD

One or more site specific standard job sheets are printed. e.g. a single
start sheet is printed, or both start and end sheets are printed.

---

### Constructor Details

#### protected JobSheets​(int value)

Construct a new job sheets enumeration value with the given integer
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

JobSheets

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

JobSheets

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

JobSheets

and any vendor-defined subclasses, the
category is class

JobSheets

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

JobSheets

and any vendor-defined subclasses, the
category name is

"job-sheets"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class JobSheets

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.JobSheets

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.JobSheets

javax.print.attribute.standard.JobSheets

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintJobAttribute

,

PrintRequestAttribute

```java
public class
JobSheets

extends
EnumSyntax

implements
PrintRequestAttribute
,
PrintJobAttribute
```

Class

JobSheets

is a printing attribute class, an enumeration, that
determines which job start and end sheets, if any, must be printed with a
job. Class

JobSheets

declares keywords for standard job sheets
values. Implementation- or site-defined names for a job sheets attribute may
also be created by defining a subclass of class

JobSheets

.

The effect of a

JobSheets

attribute on multidoc print jobs (jobs with
multiple documents) may be affected by the

MultipleDocumentHandling

job attribute,
depending on the meaning of the particular

JobSheets

value.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value. For a subclass, the attribute value must be localized to
give the IPP name and natural language values.

**See Also:** Serialized Form

public class

JobSheets

extends

EnumSyntax

implements

PrintRequestAttribute

,

PrintJobAttribute

Class

JobSheets

is a printing attribute class, an enumeration, that
determines which job start and end sheets, if any, must be printed with a
job. Class

JobSheets

declares keywords for standard job sheets
values. Implementation- or site-defined names for a job sheets attribute may
also be created by defining a subclass of class

JobSheets

.

The effect of a

JobSheets

attribute on multidoc print jobs (jobs with
multiple documents) may be affected by the

MultipleDocumentHandling

job attribute,
depending on the meaning of the particular

JobSheets

value.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value. For a subclass, the attribute value must be localized to
give the IPP name and natural language values.

The effect of a

JobSheets

attribute on multidoc print jobs (jobs with
multiple documents) may be affected by the

MultipleDocumentHandling

job attribute,
depending on the meaning of the particular

JobSheets

value.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value. For a subclass, the attribute value must be localized to
give the IPP name and natural language values.

IPP Compatibility:

The category name returned by

getName()

is
the IPP attribute name. The enumeration's integer value is the IPP enum
value. The

toString()

method returns the IPP string representation of
the attribute value. For a subclass, the attribute value must be localized to
give the IPP name and natural language values.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

JobSheets

NONE

No job sheets are printed.

static

JobSheets

STANDARD

One or more site specific standard job sheets are printed. e.g. a single
start sheet is printed, or both start and end sheets are printed.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

JobSheets

​(int value)

Construct a new job sheets enumeration value with the given integer
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

JobSheets

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

JobSheets

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

JobSheets

NONE

No job sheets are printed.

static

JobSheets

STANDARD

One or more site specific standard job sheets are printed. e.g. a single
start sheet is printed, or both start and end sheets are printed.

---

#### Field Summary

No job sheets are printed.

One or more site specific standard job sheets are printed. e.g. a single
start sheet is printed, or both start and end sheets are printed.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

JobSheets

​(int value)

Construct a new job sheets enumeration value with the given integer
value.

---

#### Constructor Summary

Construct a new job sheets enumeration value with the given integer
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

JobSheets

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

JobSheets

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

JobSheets

.

Get the name of the category of which this attribute value is an
instance.

Returns the string table for class

JobSheets

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
JobSheets
NONE
```

No job sheets are printed.

- STANDARD

```java
public static final
JobSheets
STANDARD
```

One or more site specific standard job sheets are printed. e.g. a single
start sheet is printed, or both start and end sheets are printed.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JobSheets

```java
protected JobSheets​(int value)
```

Construct a new job sheets enumeration value with the given integer
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

JobSheets

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

JobSheets

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

JobSheets

and any vendor-defined subclasses, the
category is class

JobSheets

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

JobSheets

and any vendor-defined subclasses, the
category name is

"job-sheets"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Field Detail

- NONE

```java
public static final
JobSheets
NONE
```

No job sheets are printed.

- STANDARD

```java
public static final
JobSheets
STANDARD
```

One or more site specific standard job sheets are printed. e.g. a single
start sheet is printed, or both start and end sheets are printed.

---

#### Field Detail

NONE

```java
public static final
JobSheets
NONE
```

No job sheets are printed.

---

#### NONE

public static final

JobSheets

NONE

No job sheets are printed.

STANDARD

```java
public static final
JobSheets
STANDARD
```

One or more site specific standard job sheets are printed. e.g. a single
start sheet is printed, or both start and end sheets are printed.

---

#### STANDARD

public static final

JobSheets

STANDARD

One or more site specific standard job sheets are printed. e.g. a single
start sheet is printed, or both start and end sheets are printed.

Constructor Detail

- JobSheets

```java
protected JobSheets​(int value)
```

Construct a new job sheets enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

JobSheets

```java
protected JobSheets​(int value)
```

Construct a new job sheets enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### JobSheets

protected JobSheets​(int value)

Construct a new job sheets enumeration value with the given integer
value.

Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

JobSheets

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

JobSheets

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

JobSheets

and any vendor-defined subclasses, the
category is class

JobSheets

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

JobSheets

and any vendor-defined subclasses, the
category name is

"job-sheets"

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

JobSheets

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

JobSheets

.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

JobSheets

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

JobSheets

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

JobSheets

and any vendor-defined subclasses, the
category is class

JobSheets

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

JobSheets

and any vendor-defined subclasses, the
category is class

JobSheets

itself.

For class

JobSheets

and any vendor-defined subclasses, the
category is class

JobSheets

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

JobSheets

and any vendor-defined subclasses, the
category name is

"job-sheets"

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

JobSheets

and any vendor-defined subclasses, the
category name is

"job-sheets"

.

For class

JobSheets

and any vendor-defined subclasses, the
category name is

"job-sheets"

.

---

