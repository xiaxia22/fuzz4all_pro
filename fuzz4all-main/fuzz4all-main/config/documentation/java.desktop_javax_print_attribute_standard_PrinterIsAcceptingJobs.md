# Class PrinterIsAcceptingJobs

**Source:** `java.desktop\javax\print\attribute\standard\PrinterIsAcceptingJobs.html`

### Class Description

```java
public final class
PrinterIsAcceptingJobs

extends
EnumSyntax

implements
PrintServiceAttribute
```

Class

PrinterIsAcceptingJobs

is a printing attribute class, an
enumeration, that indicates whether the printer is currently able to accept
jobs. This value is independent of the

PrinterState

and

PrinterStateReasons

attributes because its value
does not affect the current job; rather it affects future jobs. If the value
is

NOT_ACCEPTING_JOBS

, the printer will reject jobs even when the

PrinterState

is

IDLE

. If value is

ACCEPTING_JOBS

, the Printer will accept jobs even when the

PrinterState

is

STOPPED

.

IPP Compatibility:

The IPP boolean value is "true" for

ACCEPTING_JOBS

and "false" for

NOT_ACCEPTING_JOBS

. The
category name returned by

getName()

is the IPP attribute name. The
enumeration's integer value is the IPP enum value. The

toString()

method returns the IPP string representation of the attribute value.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintServiceAttribute

---

### Field Details

#### public static final
PrinterIsAcceptingJobs
NOT_ACCEPTING_JOBS

The printer is currently rejecting any jobs sent to it.

---

#### public static final
PrinterIsAcceptingJobs
ACCEPTING_JOBS

The printer is currently accepting jobs.

---

### Constructor Details

#### protected PrinterIsAcceptingJobs​(int value)

Construct a new printer is accepting jobs enumeration value with the
given integer value.

**Parameters:**
- value

- Integer value

---

### Method Details

#### protected
String
[] getStringTable()

Returns the string table for class

PrinterIsAcceptingJobs

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

PrinterIsAcceptingJobs

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

PrinterIsAcceptingJobs

, the category is class

PrinterIsAcceptingJobs

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

PrinterIsAcceptingJobs

, the category name is

"printer-is-accepting-jobs"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class PrinterIsAcceptingJobs

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.PrinterIsAcceptingJobs

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.PrinterIsAcceptingJobs

javax.print.attribute.standard.PrinterIsAcceptingJobs

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintServiceAttribute

```java
public final class
PrinterIsAcceptingJobs

extends
EnumSyntax

implements
PrintServiceAttribute
```

Class

PrinterIsAcceptingJobs

is a printing attribute class, an
enumeration, that indicates whether the printer is currently able to accept
jobs. This value is independent of the

PrinterState

and

PrinterStateReasons

attributes because its value
does not affect the current job; rather it affects future jobs. If the value
is

NOT_ACCEPTING_JOBS

, the printer will reject jobs even when the

PrinterState

is

IDLE

. If value is

ACCEPTING_JOBS

, the Printer will accept jobs even when the

PrinterState

is

STOPPED

.

IPP Compatibility:

The IPP boolean value is "true" for

ACCEPTING_JOBS

and "false" for

NOT_ACCEPTING_JOBS

. The
category name returned by

getName()

is the IPP attribute name. The
enumeration's integer value is the IPP enum value. The

toString()

method returns the IPP string representation of the attribute value.

**See Also:** Serialized Form

public final class

PrinterIsAcceptingJobs

extends

EnumSyntax

implements

PrintServiceAttribute

Class

PrinterIsAcceptingJobs

is a printing attribute class, an
enumeration, that indicates whether the printer is currently able to accept
jobs. This value is independent of the

PrinterState

and

PrinterStateReasons

attributes because its value
does not affect the current job; rather it affects future jobs. If the value
is

NOT_ACCEPTING_JOBS

, the printer will reject jobs even when the

PrinterState

is

IDLE

. If value is

ACCEPTING_JOBS

, the Printer will accept jobs even when the

PrinterState

is

STOPPED

.

IPP Compatibility:

The IPP boolean value is "true" for

ACCEPTING_JOBS

and "false" for

NOT_ACCEPTING_JOBS

. The
category name returned by

getName()

is the IPP attribute name. The
enumeration's integer value is the IPP enum value. The

toString()

method returns the IPP string representation of the attribute value.

IPP Compatibility:

The IPP boolean value is "true" for

ACCEPTING_JOBS

and "false" for

NOT_ACCEPTING_JOBS

. The
category name returned by

getName()

is the IPP attribute name. The
enumeration's integer value is the IPP enum value. The

toString()

method returns the IPP string representation of the attribute value.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

PrinterIsAcceptingJobs

ACCEPTING_JOBS

The printer is currently accepting jobs.

static

PrinterIsAcceptingJobs

NOT_ACCEPTING_JOBS

The printer is currently rejecting any jobs sent to it.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

PrinterIsAcceptingJobs

​(int value)

Construct a new printer is accepting jobs enumeration value with the
given integer value.

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

PrinterIsAcceptingJobs

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

PrinterIsAcceptingJobs

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

PrinterIsAcceptingJobs

ACCEPTING_JOBS

The printer is currently accepting jobs.

static

PrinterIsAcceptingJobs

NOT_ACCEPTING_JOBS

The printer is currently rejecting any jobs sent to it.

---

#### Field Summary

The printer is currently accepting jobs.

The printer is currently rejecting any jobs sent to it.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

PrinterIsAcceptingJobs

​(int value)

Construct a new printer is accepting jobs enumeration value with the
given integer value.

---

#### Constructor Summary

Construct a new printer is accepting jobs enumeration value with the
given integer value.

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

PrinterIsAcceptingJobs

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

PrinterIsAcceptingJobs

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

PrinterIsAcceptingJobs

.

Get the name of the category of which this attribute value is an
instance.

Returns the string table for class

PrinterIsAcceptingJobs

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

- NOT_ACCEPTING_JOBS

```java
public static final
PrinterIsAcceptingJobs
NOT_ACCEPTING_JOBS
```

The printer is currently rejecting any jobs sent to it.

- ACCEPTING_JOBS

```java
public static final
PrinterIsAcceptingJobs
ACCEPTING_JOBS
```

The printer is currently accepting jobs.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PrinterIsAcceptingJobs

```java
protected PrinterIsAcceptingJobs​(int value)
```

Construct a new printer is accepting jobs enumeration value with the
given integer value.

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

PrinterIsAcceptingJobs

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

PrinterIsAcceptingJobs

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

PrinterIsAcceptingJobs

, the category is class

PrinterIsAcceptingJobs

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

PrinterIsAcceptingJobs

, the category name is

"printer-is-accepting-jobs"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Field Detail

- NOT_ACCEPTING_JOBS

```java
public static final
PrinterIsAcceptingJobs
NOT_ACCEPTING_JOBS
```

The printer is currently rejecting any jobs sent to it.

- ACCEPTING_JOBS

```java
public static final
PrinterIsAcceptingJobs
ACCEPTING_JOBS
```

The printer is currently accepting jobs.

---

#### Field Detail

NOT_ACCEPTING_JOBS

```java
public static final
PrinterIsAcceptingJobs
NOT_ACCEPTING_JOBS
```

The printer is currently rejecting any jobs sent to it.

---

#### NOT_ACCEPTING_JOBS

public static final

PrinterIsAcceptingJobs

NOT_ACCEPTING_JOBS

The printer is currently rejecting any jobs sent to it.

ACCEPTING_JOBS

```java
public static final
PrinterIsAcceptingJobs
ACCEPTING_JOBS
```

The printer is currently accepting jobs.

---

#### ACCEPTING_JOBS

public static final

PrinterIsAcceptingJobs

ACCEPTING_JOBS

The printer is currently accepting jobs.

Constructor Detail

- PrinterIsAcceptingJobs

```java
protected PrinterIsAcceptingJobs​(int value)
```

Construct a new printer is accepting jobs enumeration value with the
given integer value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

PrinterIsAcceptingJobs

```java
protected PrinterIsAcceptingJobs​(int value)
```

Construct a new printer is accepting jobs enumeration value with the
given integer value.

**Parameters:** value

- Integer value

---

#### PrinterIsAcceptingJobs

protected PrinterIsAcceptingJobs​(int value)

Construct a new printer is accepting jobs enumeration value with the
given integer value.

Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

PrinterIsAcceptingJobs

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

PrinterIsAcceptingJobs

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

PrinterIsAcceptingJobs

, the category is class

PrinterIsAcceptingJobs

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

PrinterIsAcceptingJobs

, the category name is

"printer-is-accepting-jobs"

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

PrinterIsAcceptingJobs

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

PrinterIsAcceptingJobs

.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

PrinterIsAcceptingJobs

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

PrinterIsAcceptingJobs

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

PrinterIsAcceptingJobs

, the category is class

PrinterIsAcceptingJobs

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

PrinterIsAcceptingJobs

, the category is class

PrinterIsAcceptingJobs

itself.

For class

PrinterIsAcceptingJobs

, the category is class

PrinterIsAcceptingJobs

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

PrinterIsAcceptingJobs

, the category name is

"printer-is-accepting-jobs"

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

PrinterIsAcceptingJobs

, the category name is

"printer-is-accepting-jobs"

.

For class

PrinterIsAcceptingJobs

, the category name is

"printer-is-accepting-jobs"

.

---

