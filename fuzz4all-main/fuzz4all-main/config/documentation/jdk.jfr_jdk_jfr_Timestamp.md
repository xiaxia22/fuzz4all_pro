# Annotation Type Timestamp

**Source:** `jdk.jfr\jdk\jfr\Timestamp.html`

### Class Description

```java
@Retention
(
RUNTIME
)

@Target
({
FIELD
,
TYPE
,
METHOD
})
public @interface
Timestamp
```

Event field annotation, specifies that the value is a point in time.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### MILLISECONDS_SINCE_EPOCH

static String The unit for the difference, measured in milliseconds, between the current
time and midnight, January 1, 1970 UTC.

---

#### TICKS

static String The unit for the number of ticks that have transpired since some arbitrary
starting date.

---

#### value

String Unit for the time stamp.

---

### Additional Sections

#### Annotation Type Timestamp

```java
@Retention
(
RUNTIME
)

@Target
({
FIELD
,
TYPE
,
METHOD
})
public @interface
Timestamp
```

Event field annotation, specifies that the value is a point in time.

**Since:** 9

@Retention

(

RUNTIME

)

@Target

({

FIELD

,

TYPE

,

METHOD

})
public @interface

Timestamp

Event field annotation, specifies that the value is a point in time.

=========== ANNOTATION TYPE FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Fields

Description

static

String

MILLISECONDS_SINCE_EPOCH

The unit for the difference, measured in milliseconds, between the current
time and midnight, January 1, 1970 UTC.

static

String

TICKS

The unit for the number of ticks that have transpired since some arbitrary
starting date.

=========== ANNOTATION TYPE OPTIONAL MEMBER SUMMARY ===========

- Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

String

value

Unit for the time stamp.

Field Summary

Fields

Modifier and Type

Fields

Description

static

String

MILLISECONDS_SINCE_EPOCH

The unit for the difference, measured in milliseconds, between the current
time and midnight, January 1, 1970 UTC.

static

String

TICKS

The unit for the number of ticks that have transpired since some arbitrary
starting date.

---

#### Field Summary

The unit for the difference, measured in milliseconds, between the current
time and midnight, January 1, 1970 UTC.

The unit for the number of ticks that have transpired since some arbitrary
starting date.

Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

String

value

Unit for the time stamp.

---

#### Optional Element Summary

Unit for the time stamp.

============ ANNOTATION TYPE FIELD DETAIL ===========

- Field Detail

- MILLISECONDS_SINCE_EPOCH

```java
static final
String
MILLISECONDS_SINCE_EPOCH
```

The unit for the difference, measured in milliseconds, between the current
time and midnight, January 1, 1970 UTC.

- - TICKS

```java
static final
String
TICKS
```

The unit for the number of ticks that have transpired since some arbitrary
starting date.

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- value

```java
String
value
```

Unit for the time stamp.

**Returns:** time stamp unit, not

null

**Default:** "MILLISECONDS_SINCE_EPOCH"

Field Detail

- MILLISECONDS_SINCE_EPOCH

```java
static final
String
MILLISECONDS_SINCE_EPOCH
```

The unit for the difference, measured in milliseconds, between the current
time and midnight, January 1, 1970 UTC.

---

#### Field Detail

MILLISECONDS_SINCE_EPOCH

```java
static final
String
MILLISECONDS_SINCE_EPOCH
```

The unit for the difference, measured in milliseconds, between the current
time and midnight, January 1, 1970 UTC.

---

#### MILLISECONDS_SINCE_EPOCH

static final

String

MILLISECONDS_SINCE_EPOCH

The unit for the difference, measured in milliseconds, between the current
time and midnight, January 1, 1970 UTC.

- TICKS

```java
static final
String
TICKS
```

The unit for the number of ticks that have transpired since some arbitrary
starting date.

TICKS

```java
static final
String
TICKS
```

The unit for the number of ticks that have transpired since some arbitrary
starting date.

---

#### TICKS

static final

String

TICKS

The unit for the number of ticks that have transpired since some arbitrary
starting date.

Element Detail

- value

```java
String
value
```

Unit for the time stamp.

**Returns:** time stamp unit, not

null

**Default:** "MILLISECONDS_SINCE_EPOCH"

---

#### Element Detail

value

```java
String
value
```

Unit for the time stamp.

**Returns:** time stamp unit, not

null

**Default:** "MILLISECONDS_SINCE_EPOCH"

---

#### value

String

value

Unit for the time stamp.

---

