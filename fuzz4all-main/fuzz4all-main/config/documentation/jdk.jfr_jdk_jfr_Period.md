# Annotation Type Period

**Source:** `jdk.jfr\jdk\jfr\Period.html`

### Class Description

```java
@Retention
(
RUNTIME
)

@Inherited

@Target
(
TYPE
)
public @interface
Period
```

Event annotation, specifies the default setting value for a periodic event.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### NAME

static String Settings name "period" for configuring periodic events

---

#### value

String Returns the default setting value for a periodic setting.

---

### Additional Sections

#### Annotation Type Period

```java
@Retention
(
RUNTIME
)

@Inherited

@Target
(
TYPE
)
public @interface
Period
```

Event annotation, specifies the default setting value for a periodic event.

**Since:** 9

@Retention

(

RUNTIME

)

@Inherited

@Target

(

TYPE

)
public @interface

Period

Event annotation, specifies the default setting value for a periodic event.

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

"period"

for configuring periodic events

=========== ANNOTATION TYPE OPTIONAL MEMBER SUMMARY ===========

- Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

String

value

Returns the default setting value for a periodic setting.

Field Summary

Fields

Modifier and Type

Fields

Description

static

String

NAME

Settings name

"period"

for configuring periodic events

---

#### Field Summary

Settings name

"period"

for configuring periodic events

Optional Element Summary

Optional Elements

Modifier and Type

Optional Element

Description

String

value

Returns the default setting value for a periodic setting.

---

#### Optional Element Summary

Returns the default setting value for a periodic setting.

============ ANNOTATION TYPE FIELD DETAIL ===========

- Field Detail

- NAME

```java
static final
String
NAME
```

Settings name

"period"

for configuring periodic events

============ ANNOTATION TYPE MEMBER DETAIL ===========

- Element Detail

- value

```java
String
value
```

Returns the default setting value for a periodic setting.

String representation of a positive

Long

value followed by an empty
space and one of the following units:

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

Example values:

"0 ns"

,

"10 ms"

, and

"1 s"

.

A period may also be

"everyChunk"

to specify that it occurs at
least once for every recording file. The number of events that are emitted
depends on how many times the file rotations occur when data is recorded.

**Returns:** the default setting value, not

null

**Default:** "everyChunk"

Field Detail

- NAME

```java
static final
String
NAME
```

Settings name

"period"

for configuring periodic events

---

#### Field Detail

NAME

```java
static final
String
NAME
```

Settings name

"period"

for configuring periodic events

---

#### NAME

static final

String

NAME

Settings name

"period"

for configuring periodic events

Element Detail

- value

```java
String
value
```

Returns the default setting value for a periodic setting.

String representation of a positive

Long

value followed by an empty
space and one of the following units:

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

Example values:

"0 ns"

,

"10 ms"

, and

"1 s"

.

A period may also be

"everyChunk"

to specify that it occurs at
least once for every recording file. The number of events that are emitted
depends on how many times the file rotations occur when data is recorded.

**Returns:** the default setting value, not

null

**Default:** "everyChunk"

---

#### Element Detail

value

```java
String
value
```

Returns the default setting value for a periodic setting.

String representation of a positive

Long

value followed by an empty
space and one of the following units:

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

Example values:

"0 ns"

,

"10 ms"

, and

"1 s"

.

A period may also be

"everyChunk"

to specify that it occurs at
least once for every recording file. The number of events that are emitted
depends on how many times the file rotations occur when data is recorded.

**Returns:** the default setting value, not

null

**Default:** "everyChunk"

---

#### value

String

value

Returns the default setting value for a periodic setting.

String representation of a positive

Long

value followed by an empty
space and one of the following units:

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

Example values:

"0 ns"

,

"10 ms"

, and

"1 s"

.

A period may also be

"everyChunk"

to specify that it occurs at
least once for every recording file. The number of events that are emitted
depends on how many times the file rotations occur when data is recorded.

String representation of a positive

Long

value followed by an empty
space and one of the following units:

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

Example values:

"0 ns"

,

"10 ms"

, and

"1 s"

.

A period may also be

"everyChunk"

to specify that it occurs at
least once for every recording file. The number of events that are emitted
depends on how many times the file rotations occur when data is recorded.

Example values:

"0 ns"

,

"10 ms"

, and

"1 s"

.

A period may also be

"everyChunk"

to specify that it occurs at
least once for every recording file. The number of events that are emitted
depends on how many times the file rotations occur when data is recorded.

A period may also be

"everyChunk"

to specify that it occurs at
least once for every recording file. The number of events that are emitted
depends on how many times the file rotations occur when data is recorded.

---

