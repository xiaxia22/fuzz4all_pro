# Annotation Type Generated

**Source:** `java.compiler\javax\annotation\processing\Generated.html`

### Class Description

```java
@Documented

@Retention
(
SOURCE
)

@Target
({
PACKAGE
,
TYPE
,
METHOD
,
CONSTRUCTOR
,
FIELD
,
LOCAL_VARIABLE
,
PARAMETER
})
public @interface
Generated
```

The Generated annotation is used to mark source code that has been generated.
It can also be used to differentiate user written code from generated code in
a single file.

Examples:

```java
@Generated("com.example.Generator")
```

```java
@Generated(value="com.example.Generator", date= "2017-07-04T12:08:56.235-0700")
```

```java
@Generated(value="com.example.Generator", date= "2017-07-04T12:08:56.235-0700",
comments= "comment 1")
```

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### value

String [] The value element MUST have the name of the code generator.

---

#### comments

String A place holder for any comments that the code generator may want to
include in the generated code.

---

#### date

String Date when the source was generated.

---

### Additional Sections

#### Annotation Type Generated

```java
@Documented

@Retention
(
SOURCE
)

@Target
({
PACKAGE
,
TYPE
,
METHOD
,
CONSTRUCTOR
,
FIELD
,
LOCAL_VARIABLE
,
PARAMETER
})
public @interface
Generated
```

The Generated annotation is used to mark source code that has been generated.
It can also be used to differentiate user written code from generated code in
a single file.

Examples:

```java
@Generated("com.example.Generator")
```

```java
@Generated(value="com.example.Generator", date= "2017-07-04T12:08:56.235-0700")
```

```java
@Generated(value="com.example.Generator", date= "2017-07-04T12:08:56.235-0700",
comments= "comment 1")
```

**Since:** 9

@Documented

@Retention

(

SOURCE

)

@Target

({

PACKAGE

,

TYPE

,

METHOD

,

CONSTRUCTOR

,

FIELD

,

LOCAL_VARIABLE

,

PARAMETER

})
public @interface

Generated

The Generated annotation is used to mark source code that has been generated.
It can also be used to differentiate user written code from generated code in
a single file.

Examples:

```java
@Generated("com.example.Generator")
```

```java
@Generated(value="com.example.Generator", date= "2017-07-04T12:08:56.235-0700")
```

```java
@Generated(value="com.example.Generator", date= "2017-07-04T12:08:56.235-0700",
comments= "comment 1")
```

---

#### Examples:

@Generated("com.example.Generator")

@Generated(value="com.example.Generator", date= "2017-07-04T12:08:56.235-0700")

@Generated(value="com.example.Generator", date= "2017-07-04T12:08:56.235-0700",
comments= "comment 1")

=========== ANNOTATION TYPE REQUIRED MEMBER SUMMARY ===========

- Required Element Summary

Required Elements

Modifier and Type

Required Element

Description

String

[]

value

The value element MUST have the name of the code generator.

=========== ANNOTATION TYPE OPTIONAL MEMBER SUMMARY ===========

- Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

String

comments

A place holder for any comments that the code generator may want to
include in the generated code.

String

date

Date when the source was generated.

Required Element Summary

Required Elements

Modifier and Type

Required Element

Description

String

[]

value

The value element MUST have the name of the code generator.

---

#### Required Element Summary

The value element MUST have the name of the code generator.

Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

String

comments

A place holder for any comments that the code generator may want to
include in the generated code.

String

date

Date when the source was generated.

---

#### Optional Element Summary

A place holder for any comments that the code generator may want to
include in the generated code.

Date when the source was generated.

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- value

```java
String
[] value
```

The value element MUST have the name of the code generator. The
name is the fully qualified name of the code generator.

**Returns:** The name of the code generator

============ ANNOTATION TYPE MEMBER DETAIL ===========

- - date

```java
String
date
```

Date when the source was generated. The date element must follow the ISO
8601 standard. For example the date element would have the following
value 2017-07-04T12:08:56.235-0700 which represents 2017-07-04 12:08:56
local time in the U.S. Pacific Time time zone.

**Returns:** The date the source was generated

**Default:** ""

- - comments

```java
String
comments
```

A place holder for any comments that the code generator may want to
include in the generated code.

**Returns:** Comments that the code generated included

**Default:** ""

Element Detail

- value

```java
String
[] value
```

The value element MUST have the name of the code generator. The
name is the fully qualified name of the code generator.

**Returns:** The name of the code generator

---

#### Element Detail

value

```java
String
[] value
```

The value element MUST have the name of the code generator. The
name is the fully qualified name of the code generator.

**Returns:** The name of the code generator

---

#### value

String

[] value

The value element MUST have the name of the code generator. The
name is the fully qualified name of the code generator.

- date

```java
String
date
```

Date when the source was generated. The date element must follow the ISO
8601 standard. For example the date element would have the following
value 2017-07-04T12:08:56.235-0700 which represents 2017-07-04 12:08:56
local time in the U.S. Pacific Time time zone.

**Returns:** The date the source was generated

**Default:** ""

date

```java
String
date
```

Date when the source was generated. The date element must follow the ISO
8601 standard. For example the date element would have the following
value 2017-07-04T12:08:56.235-0700 which represents 2017-07-04 12:08:56
local time in the U.S. Pacific Time time zone.

**Returns:** The date the source was generated

**Default:** ""

---

#### date

String

date

Date when the source was generated. The date element must follow the ISO
8601 standard. For example the date element would have the following
value 2017-07-04T12:08:56.235-0700 which represents 2017-07-04 12:08:56
local time in the U.S. Pacific Time time zone.

- comments

```java
String
comments
```

A place holder for any comments that the code generator may want to
include in the generated code.

**Returns:** Comments that the code generated included

**Default:** ""

comments

```java
String
comments
```

A place holder for any comments that the code generator may want to
include in the generated code.

**Returns:** Comments that the code generated included

**Default:** ""

---

#### comments

String

comments

A place holder for any comments that the code generator may want to
include in the generated code.

---

