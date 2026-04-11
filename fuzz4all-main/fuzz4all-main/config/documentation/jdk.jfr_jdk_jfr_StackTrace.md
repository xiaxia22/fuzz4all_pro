# Annotation Type StackTrace

**Source:** `jdk.jfr\jdk\jfr\StackTrace.html`

### Class Description

```java
@Target
(
TYPE
)

@Inherited

@Retention
(
RUNTIME
)
public @interface
StackTrace
```

Event annotation, determines whether an event by default has a stack trace
or not.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### NAME

static String Settings name "stackTrace" to be used for enabling event stack traces.

---

#### value

boolean Returns if the stack trace from the Event#commit() method should be recorded.

---

### Additional Sections

#### Annotation Type StackTrace

```java
@Target
(
TYPE
)

@Inherited

@Retention
(
RUNTIME
)
public @interface
StackTrace
```

Event annotation, determines whether an event by default has a stack trace
or not.

**Since:** 9

@Target

(

TYPE

)

@Inherited

@Retention

(

RUNTIME

)
public @interface

StackTrace

Event annotation, determines whether an event by default has a stack trace
or not.

=========== ANNOTATION TYPE FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Fields

Description

static

String

NAME

Settings name

"stackTrace"

to be used for enabling event stack traces.

=========== ANNOTATION TYPE OPTIONAL MEMBER SUMMARY ===========

- Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

boolean

value

Returns if the stack trace from the

Event#commit()

method should be recorded.

Field Summary

Fields

Modifier and Type

Fields

Description

static

String

NAME

Settings name

"stackTrace"

to be used for enabling event stack traces.

---

#### Field Summary

Settings name

"stackTrace"

to be used for enabling event stack traces.

Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

boolean

value

Returns if the stack trace from the

Event#commit()

method should be recorded.

---

#### Optional Element Summary

Returns if the stack trace from the

Event#commit()

method should be recorded.

============ ANNOTATION TYPE FIELD DETAIL ===========

- Field Detail

- NAME

```java
static final
String
NAME
```

Settings name

"stackTrace"

to be used for enabling event stack traces.

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- value

```java
boolean value
```

Returns if the stack trace from the

Event#commit()

method should be recorded.

**Returns:** true

if the stack trace should be recorded,

false

otherwise

**Default:** true

Field Detail

- NAME

```java
static final
String
NAME
```

Settings name

"stackTrace"

to be used for enabling event stack traces.

---

#### Field Detail

NAME

```java
static final
String
NAME
```

Settings name

"stackTrace"

to be used for enabling event stack traces.

---

#### NAME

static final

String

NAME

Settings name

"stackTrace"

to be used for enabling event stack traces.

Element Detail

- value

```java
boolean value
```

Returns if the stack trace from the

Event#commit()

method should be recorded.

**Returns:** true

if the stack trace should be recorded,

false

otherwise

**Default:** true

---

#### Element Detail

value

```java
boolean value
```

Returns if the stack trace from the

Event#commit()

method should be recorded.

**Returns:** true

if the stack trace should be recorded,

false

otherwise

**Default:** true

---

#### value

boolean value

Returns if the stack trace from the

Event#commit()

method should be recorded.

---

