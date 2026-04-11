# Interface WatchEvent<T>

**Source:** `java.base\java\nio\file\WatchEvent.html`

### Class Description

```java
public interface
WatchEvent<T>
```

An event or a repeated event for an object that is registered with a

WatchService

.

An event is classified by its

kind

and has a

count

to indicate the number of times that the event has been
observed. This allows for efficient representation of repeated events. The

context

method returns any context associated with
the event. In the case of a repeated event then the context is the same for
all events.

Watch events are immutable and safe for use by multiple concurrent
threads.

**Type Parameters:** T

- The type of the context object associated with the event

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### WatchEvent.Kind
<
T
> kind()

Returns the event kind.

**Returns:**
- the event kind

---

#### int count()

Returns the event count. If the event count is greater than

1

then this is a repeated event.

**Returns:**
- the event count

---

#### T
context()

Returns the context for the event.

In the case of

ENTRY_CREATE

,

ENTRY_DELETE

, and

ENTRY_MODIFY

events the context is
a

Path

that is the

relative

path between
the directory registered with the watch service, and the entry that is
created, deleted, or modified.

**Returns:**
- the event context; may be

null

---

### Additional Sections

#### Interface WatchEvent<T>

**Type Parameters:** T

- The type of the context object associated with the event

```java
public interface
WatchEvent<T>
```

An event or a repeated event for an object that is registered with a

WatchService

.

An event is classified by its

kind

and has a

count

to indicate the number of times that the event has been
observed. This allows for efficient representation of repeated events. The

context

method returns any context associated with
the event. In the case of a repeated event then the context is the same for
all events.

Watch events are immutable and safe for use by multiple concurrent
threads.

**Since:** 1.7

public interface

WatchEvent<T>

An event or a repeated event for an object that is registered with a

WatchService

.

An event is classified by its

kind

and has a

count

to indicate the number of times that the event has been
observed. This allows for efficient representation of repeated events. The

context

method returns any context associated with
the event. In the case of a repeated event then the context is the same for
all events.

Watch events are immutable and safe for use by multiple concurrent
threads.

An event is classified by its

kind

and has a

count

to indicate the number of times that the event has been
observed. This allows for efficient representation of repeated events. The

context

method returns any context associated with
the event. In the case of a repeated event then the context is the same for
all events.

Watch events are immutable and safe for use by multiple concurrent
threads.

Watch events are immutable and safe for use by multiple concurrent
threads.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

WatchEvent.Kind

<

T

>

An event kind, for the purposes of identification.

static interface

WatchEvent.Modifier

An event modifier that qualifies how a

Watchable

is registered
with a

WatchService

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

T

context

()

Returns the context for the event.

int

count

()

Returns the event count.

WatchEvent.Kind

<

T

>

kind

()

Returns the event kind.

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

WatchEvent.Kind

<

T

>

An event kind, for the purposes of identification.

static interface

WatchEvent.Modifier

An event modifier that qualifies how a

Watchable

is registered
with a

WatchService

.

---

#### Nested Class Summary

An event kind, for the purposes of identification.

An event modifier that qualifies how a

Watchable

is registered
with a

WatchService

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

T

context

()

Returns the context for the event.

int

count

()

Returns the event count.

WatchEvent.Kind

<

T

>

kind

()

Returns the event kind.

---

#### Method Summary

Returns the context for the event.

Returns the event count.

Returns the event kind.

============ METHOD DETAIL ==========

- Method Detail

- kind

```java
WatchEvent.Kind
<
T
> kind()
```

Returns the event kind.

**Returns:** the event kind

- count

```java
int count()
```

Returns the event count. If the event count is greater than

1

then this is a repeated event.

**Returns:** the event count

- context

```java
T
context()
```

Returns the context for the event.

In the case of

ENTRY_CREATE

,

ENTRY_DELETE

, and

ENTRY_MODIFY

events the context is
a

Path

that is the

relative

path between
the directory registered with the watch service, and the entry that is
created, deleted, or modified.

**Returns:** the event context; may be

null

Method Detail

- kind

```java
WatchEvent.Kind
<
T
> kind()
```

Returns the event kind.

**Returns:** the event kind

- count

```java
int count()
```

Returns the event count. If the event count is greater than

1

then this is a repeated event.

**Returns:** the event count

- context

```java
T
context()
```

Returns the context for the event.

In the case of

ENTRY_CREATE

,

ENTRY_DELETE

, and

ENTRY_MODIFY

events the context is
a

Path

that is the

relative

path between
the directory registered with the watch service, and the entry that is
created, deleted, or modified.

**Returns:** the event context; may be

null

---

#### Method Detail

kind

```java
WatchEvent.Kind
<
T
> kind()
```

Returns the event kind.

**Returns:** the event kind

---

#### kind

WatchEvent.Kind

<

T

> kind()

Returns the event kind.

count

```java
int count()
```

Returns the event count. If the event count is greater than

1

then this is a repeated event.

**Returns:** the event count

---

#### count

int count()

Returns the event count. If the event count is greater than

1

then this is a repeated event.

context

```java
T
context()
```

Returns the context for the event.

In the case of

ENTRY_CREATE

,

ENTRY_DELETE

, and

ENTRY_MODIFY

events the context is
a

Path

that is the

relative

path between
the directory registered with the watch service, and the entry that is
created, deleted, or modified.

**Returns:** the event context; may be

null

---

#### context

T

context()

Returns the context for the event.

In the case of

ENTRY_CREATE

,

ENTRY_DELETE

, and

ENTRY_MODIFY

events the context is
a

Path

that is the

relative

path between
the directory registered with the watch service, and the entry that is
created, deleted, or modified.

In the case of

ENTRY_CREATE

,

ENTRY_DELETE

, and

ENTRY_MODIFY

events the context is
a

Path

that is the

relative

path between
the directory registered with the watch service, and the entry that is
created, deleted, or modified.

---

