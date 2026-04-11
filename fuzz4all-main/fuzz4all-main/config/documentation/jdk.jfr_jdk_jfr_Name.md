# Annotation Type Name

**Source:** `jdk.jfr\jdk\jfr\Name.html`

### Class Description

```java
@Target
({
TYPE
,
FIELD
,
METHOD
})

@Retention
(
RUNTIME
)
public @interface
Name
```

Annotation that overrides the default name for an element (for example, when
the default package for an event is not appropriate).

The name must be a valid identifiers in the Java language (for example,

"com.example.MyEvent"

for an event class or

"message"

for an
event field).

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### value

String Returns the name.

---

### Additional Sections

#### Annotation Type Name

```java
@Target
({
TYPE
,
FIELD
,
METHOD
})

@Retention
(
RUNTIME
)
public @interface
Name
```

Annotation that overrides the default name for an element (for example, when
the default package for an event is not appropriate).

The name must be a valid identifiers in the Java language (for example,

"com.example.MyEvent"

for an event class or

"message"

for an
event field).

**Since:** 9

@Target

({

TYPE

,

FIELD

,

METHOD

})

@Retention

(

RUNTIME

)
public @interface

Name

Annotation that overrides the default name for an element (for example, when
the default package for an event is not appropriate).

The name must be a valid identifiers in the Java language (for example,

"com.example.MyEvent"

for an event class or

"message"

for an
event field).

The name must be a valid identifiers in the Java language (for example,

"com.example.MyEvent"

for an event class or

"message"

for an
event field).

=========== ANNOTATION TYPE REQUIRED MEMBER SUMMARY ===========

- Required Element Summary

Required Elements

Modifier and Type

Required Element

Description

String

value

Returns the name.

Required Element Summary

Required Elements

Modifier and Type

Required Element

Description

String

value

Returns the name.

---

#### Required Element Summary

Returns the name.

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- value

```java
String
value
```

Returns the name.

**Returns:** the name

Element Detail

- value

```java
String
value
```

Returns the name.

**Returns:** the name

---

#### Element Detail

value

```java
String
value
```

Returns the name.

**Returns:** the name

---

#### value

String

value

Returns the name.

---

