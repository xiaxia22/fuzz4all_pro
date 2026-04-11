# Class PrinterState

**Source:** `java.desktop\javax\print\attribute\standard\PrinterState.html`

### Class Description

```java
public final class
PrinterState

extends
EnumSyntax

implements
PrintServiceAttribute
```

Class

PrinterState

is a printing attribute class, an enumeration,
that identifies the current state of a printer. Class

PrinterState

defines standard printer state values. A Print Service implementation only
needs to report those printer states which are appropriate for the particular
implementation; it does not have to report every defined printer state. The

PrinterStateReasons

attribute augments the

PrinterState

attribute to give more detailed information about the
printer in given printer state.

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

PrintServiceAttribute

---

### Field Details

#### public static final
PrinterState
UNKNOWN

The printer state is unknown.

---

#### public static final
PrinterState
IDLE

Indicates that new jobs can start processing without waiting.

---

#### public static final
PrinterState
PROCESSING

Indicates that jobs are processing; new jobs will wait before processing.

---

#### public static final
PrinterState
STOPPED

Indicates that no jobs can be processed and intervention is required.

---

### Constructor Details

#### protected PrinterState​(int value)

Construct a new printer state enumeration value with the given integer
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

PrinterState

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

PrinterState

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

PrinterState

, the category is class

PrinterState

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

PrinterState

, the category name is

"printer-state"

.

**Specified by:**
- getName

in interface

Attribute

**Returns:**
- attribute category name

---

### Additional Sections

#### Class PrinterState

java.lang.Object

- javax.print.attribute.EnumSyntax
- - javax.print.attribute.standard.PrinterState

javax.print.attribute.EnumSyntax

- javax.print.attribute.standard.PrinterState

javax.print.attribute.standard.PrinterState

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Attribute

,

PrintServiceAttribute

```java
public final class
PrinterState

extends
EnumSyntax

implements
PrintServiceAttribute
```

Class

PrinterState

is a printing attribute class, an enumeration,
that identifies the current state of a printer. Class

PrinterState

defines standard printer state values. A Print Service implementation only
needs to report those printer states which are appropriate for the particular
implementation; it does not have to report every defined printer state. The

PrinterStateReasons

attribute augments the

PrinterState

attribute to give more detailed information about the
printer in given printer state.

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

public final class

PrinterState

extends

EnumSyntax

implements

PrintServiceAttribute

Class

PrinterState

is a printing attribute class, an enumeration,
that identifies the current state of a printer. Class

PrinterState

defines standard printer state values. A Print Service implementation only
needs to report those printer states which are appropriate for the particular
implementation; it does not have to report every defined printer state. The

PrinterStateReasons

attribute augments the

PrinterState

attribute to give more detailed information about the
printer in given printer state.

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

PrinterState

IDLE

Indicates that new jobs can start processing without waiting.

static

PrinterState

PROCESSING

Indicates that jobs are processing; new jobs will wait before processing.

static

PrinterState

STOPPED

Indicates that no jobs can be processed and intervention is required.

static

PrinterState

UNKNOWN

The printer state is unknown.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

PrinterState

​(int value)

Construct a new printer state enumeration value with the given integer
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

PrinterState

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

PrinterState

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

PrinterState

IDLE

Indicates that new jobs can start processing without waiting.

static

PrinterState

PROCESSING

Indicates that jobs are processing; new jobs will wait before processing.

static

PrinterState

STOPPED

Indicates that no jobs can be processed and intervention is required.

static

PrinterState

UNKNOWN

The printer state is unknown.

---

#### Field Summary

Indicates that new jobs can start processing without waiting.

Indicates that jobs are processing; new jobs will wait before processing.

Indicates that no jobs can be processed and intervention is required.

The printer state is unknown.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

PrinterState

​(int value)

Construct a new printer state enumeration value with the given integer
value.

---

#### Constructor Summary

Construct a new printer state enumeration value with the given integer
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

PrinterState

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

PrinterState

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

PrinterState

.

Get the name of the category of which this attribute value is an
instance.

Returns the string table for class

PrinterState

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

- UNKNOWN

```java
public static final
PrinterState
UNKNOWN
```

The printer state is unknown.

- IDLE

```java
public static final
PrinterState
IDLE
```

Indicates that new jobs can start processing without waiting.

- PROCESSING

```java
public static final
PrinterState
PROCESSING
```

Indicates that jobs are processing; new jobs will wait before processing.

- STOPPED

```java
public static final
PrinterState
STOPPED
```

Indicates that no jobs can be processed and intervention is required.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PrinterState

```java
protected PrinterState​(int value)
```

Construct a new printer state enumeration value with the given integer
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

PrinterState

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

PrinterState

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

PrinterState

, the category is class

PrinterState

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

PrinterState

, the category name is

"printer-state"

.

**Specified by:** getName

in interface

Attribute
**Returns:** attribute category name

Field Detail

- UNKNOWN

```java
public static final
PrinterState
UNKNOWN
```

The printer state is unknown.

- IDLE

```java
public static final
PrinterState
IDLE
```

Indicates that new jobs can start processing without waiting.

- PROCESSING

```java
public static final
PrinterState
PROCESSING
```

Indicates that jobs are processing; new jobs will wait before processing.

- STOPPED

```java
public static final
PrinterState
STOPPED
```

Indicates that no jobs can be processed and intervention is required.

---

#### Field Detail

UNKNOWN

```java
public static final
PrinterState
UNKNOWN
```

The printer state is unknown.

---

#### UNKNOWN

public static final

PrinterState

UNKNOWN

The printer state is unknown.

IDLE

```java
public static final
PrinterState
IDLE
```

Indicates that new jobs can start processing without waiting.

---

#### IDLE

public static final

PrinterState

IDLE

Indicates that new jobs can start processing without waiting.

PROCESSING

```java
public static final
PrinterState
PROCESSING
```

Indicates that jobs are processing; new jobs will wait before processing.

---

#### PROCESSING

public static final

PrinterState

PROCESSING

Indicates that jobs are processing; new jobs will wait before processing.

STOPPED

```java
public static final
PrinterState
STOPPED
```

Indicates that no jobs can be processed and intervention is required.

---

#### STOPPED

public static final

PrinterState

STOPPED

Indicates that no jobs can be processed and intervention is required.

Constructor Detail

- PrinterState

```java
protected PrinterState​(int value)
```

Construct a new printer state enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### Constructor Detail

PrinterState

```java
protected PrinterState​(int value)
```

Construct a new printer state enumeration value with the given integer
value.

**Parameters:** value

- Integer value

---

#### PrinterState

protected PrinterState​(int value)

Construct a new printer state enumeration value with the given integer
value.

Method Detail

- getStringTable

```java
protected
String
[] getStringTable()
```

Returns the string table for class

PrinterState

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

PrinterState

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

PrinterState

, the category is class

PrinterState

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

PrinterState

, the category name is

"printer-state"

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

PrinterState

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

PrinterState

.

getEnumValueTable

```java
protected
EnumSyntax
[] getEnumValueTable()
```

Returns the enumeration value table for class

PrinterState

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

PrinterState

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

PrinterState

, the category is class

PrinterState

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

PrinterState

, the category is class

PrinterState

itself.

For class

PrinterState

, the category is class

PrinterState

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

PrinterState

, the category name is

"printer-state"

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

PrinterState

, the category name is

"printer-state"

.

For class

PrinterState

, the category name is

"printer-state"

.

---

