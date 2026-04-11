# Annotation Type Threshold

**Source:** `jdk.jfr\jdk\jfr\Threshold.html`

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
Threshold
```

Event annotation, specifies the default duration below which an event is not
recorded (for example,

"20 ms"

).

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### NAME

static String Setting name "threshold" for configuring event thresholds.

---

#### value

String The threshold (for example, "20 ms" ).

---

### Additional Sections

#### Annotation Type Threshold

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
Threshold
```

Event annotation, specifies the default duration below which an event is not
recorded (for example,

"20 ms"

).

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

Threshold

Event annotation, specifies the default duration below which an event is not
recorded (for example,

"20 ms"

).

=========== ANNOTATION TYPE FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Fields

Description

static

String

NAME

Setting name

"threshold"

for configuring event thresholds.

=========== ANNOTATION TYPE OPTIONAL MEMBER SUMMARY ===========

- Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

String

value

The threshold (for example,

"20 ms"

).

Field Summary

Fields

Modifier and Type

Fields

Description

static

String

NAME

Setting name

"threshold"

for configuring event thresholds.

---

#### Field Summary

Setting name

"threshold"

for configuring event thresholds.

Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

String

value

The threshold (for example,

"20 ms"

).

---

#### Optional Element Summary

The threshold (for example,

"20 ms"

).

============ ANNOTATION TYPE FIELD DETAIL ===========

- Field Detail

- NAME

```java
static final
String
NAME
```

Setting name

"threshold"

for configuring event thresholds.

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- value

```java
String
value
```

The threshold (for example,

"20 ms"

).

A

String

representation of a positive

Long

value followed by an
empty space and one of the following units:

"ns"

(nanoseconds)

"us"

(microseconds)

"ms"

(milliseconds)

"s"

(seconds)

"m"

(minutes)

"h"

(hours)

"d"

(days)

Example values are

"0 ns"

,

"10 ms"

, and

"1 s"

.

**Returns:** the threshold, default

"0 ns"

, not

null

**Default:** "0 ns"

Field Detail

- NAME

```java
static final
String
NAME
```

Setting name

"threshold"

for configuring event thresholds.

---

#### Field Detail

NAME

```java
static final
String
NAME
```

Setting name

"threshold"

for configuring event thresholds.

---

#### NAME

static final

String

NAME

Setting name

"threshold"

for configuring event thresholds.

Element Detail

- value

```java
String
value
```

The threshold (for example,

"20 ms"

).

A

String

representation of a positive

Long

value followed by an
empty space and one of the following units:

"ns"

(nanoseconds)

"us"

(microseconds)

"ms"

(milliseconds)

"s"

(seconds)

"m"

(minutes)

"h"

(hours)

"d"

(days)

Example values are

"0 ns"

,

"10 ms"

, and

"1 s"

.

**Returns:** the threshold, default

"0 ns"

, not

null

**Default:** "0 ns"

---

#### Element Detail

value

```java
String
value
```

The threshold (for example,

"20 ms"

).

A

String

representation of a positive

Long

value followed by an
empty space and one of the following units:

"ns"

(nanoseconds)

"us"

(microseconds)

"ms"

(milliseconds)

"s"

(seconds)

"m"

(minutes)

"h"

(hours)

"d"

(days)

Example values are

"0 ns"

,

"10 ms"

, and

"1 s"

.

**Returns:** the threshold, default

"0 ns"

, not

null

**Default:** "0 ns"

---

#### value

String

value

The threshold (for example,

"20 ms"

).

A

String

representation of a positive

Long

value followed by an
empty space and one of the following units:

"ns"

(nanoseconds)

"us"

(microseconds)

"ms"

(milliseconds)

"s"

(seconds)

"m"

(minutes)

"h"

(hours)

"d"

(days)

Example values are

"0 ns"

,

"10 ms"

, and

"1 s"

.

A

String

representation of a positive

Long

value followed by an
empty space and one of the following units:

"ns"

(nanoseconds)

"us"

(microseconds)

"ms"

(milliseconds)

"s"

(seconds)

"m"

(minutes)

"h"

(hours)

"d"

(days)

Example values are

"0 ns"

,

"10 ms"

, and

"1 s"

.

Example values are

"0 ns"

,

"10 ms"

, and

"1 s"

.

---

