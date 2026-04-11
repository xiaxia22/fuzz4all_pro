# Annotation Type Timespan

**Source:** `jdk.jfr\jdk\jfr\Timespan.html`

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
Timespan
```

Event field annotation, specifies that the value is a duration.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### MICROSECONDS

static String Unit for microseconds.

---

#### MILLISECONDS

static String Unit for milliseconds.

---

#### NANOSECONDS

static String Unit for nanoseconds.

---

#### SECONDS

static String Unit for seconds.

---

#### TICKS

static String Unit for ticks.

---

#### value

String Returns the unit of measure for the time span.

---

### Additional Sections

#### Annotation Type Timespan

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
Timespan
```

Event field annotation, specifies that the value is a duration.

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

Timespan

Event field annotation, specifies that the value is a duration.

=========== ANNOTATION TYPE FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Fields

Description

static

String

MICROSECONDS

Unit for microseconds.

static

String

MILLISECONDS

Unit for milliseconds.

static

String

NANOSECONDS

Unit for nanoseconds.

static

String

SECONDS

Unit for seconds.

static

String

TICKS

Unit for ticks.

=========== ANNOTATION TYPE OPTIONAL MEMBER SUMMARY ===========

- Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

String

value

Returns the unit of measure for the time span.

Field Summary

Fields

Modifier and Type

Fields

Description

static

String

MICROSECONDS

Unit for microseconds.

static

String

MILLISECONDS

Unit for milliseconds.

static

String

NANOSECONDS

Unit for nanoseconds.

static

String

SECONDS

Unit for seconds.

static

String

TICKS

Unit for ticks.

---

#### Field Summary

Unit for microseconds.

Unit for milliseconds.

Unit for nanoseconds.

Unit for seconds.

Unit for ticks.

Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

String

value

Returns the unit of measure for the time span.

---

#### Optional Element Summary

Returns the unit of measure for the time span.

============ ANNOTATION TYPE FIELD DETAIL ===========

- Field Detail

- TICKS

```java
static final
String
TICKS
```

Unit for ticks.

- - SECONDS

```java
static final
String
SECONDS
```

Unit for seconds.

- - MILLISECONDS

```java
static final
String
MILLISECONDS
```

Unit for milliseconds.

- - NANOSECONDS

```java
static final
String
NANOSECONDS
```

Unit for nanoseconds.

- - MICROSECONDS

```java
static final
String
MICROSECONDS
```

Unit for microseconds.

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- value

```java
String
value
```

Returns the unit of measure for the time span.

By default, the unit is nanoseconds.

**Returns:** the time span unit, default

#NANOSECONDS

, not

null

**Default:** "NANOSECONDS"

Field Detail

- TICKS

```java
static final
String
TICKS
```

Unit for ticks.

---

#### Field Detail

TICKS

```java
static final
String
TICKS
```

Unit for ticks.

---

#### TICKS

static final

String

TICKS

Unit for ticks.

- SECONDS

```java
static final
String
SECONDS
```

Unit for seconds.

SECONDS

```java
static final
String
SECONDS
```

Unit for seconds.

---

#### SECONDS

static final

String

SECONDS

Unit for seconds.

- MILLISECONDS

```java
static final
String
MILLISECONDS
```

Unit for milliseconds.

MILLISECONDS

```java
static final
String
MILLISECONDS
```

Unit for milliseconds.

---

#### MILLISECONDS

static final

String

MILLISECONDS

Unit for milliseconds.

- NANOSECONDS

```java
static final
String
NANOSECONDS
```

Unit for nanoseconds.

NANOSECONDS

```java
static final
String
NANOSECONDS
```

Unit for nanoseconds.

---

#### NANOSECONDS

static final

String

NANOSECONDS

Unit for nanoseconds.

- MICROSECONDS

```java
static final
String
MICROSECONDS
```

Unit for microseconds.

MICROSECONDS

```java
static final
String
MICROSECONDS
```

Unit for microseconds.

---

#### MICROSECONDS

static final

String

MICROSECONDS

Unit for microseconds.

Element Detail

- value

```java
String
value
```

Returns the unit of measure for the time span.

By default, the unit is nanoseconds.

**Returns:** the time span unit, default

#NANOSECONDS

, not

null

**Default:** "NANOSECONDS"

---

#### Element Detail

value

```java
String
value
```

Returns the unit of measure for the time span.

By default, the unit is nanoseconds.

**Returns:** the time span unit, default

#NANOSECONDS

, not

null

**Default:** "NANOSECONDS"

---

#### value

String

value

Returns the unit of measure for the time span.

By default, the unit is nanoseconds.

By default, the unit is nanoseconds.

---

