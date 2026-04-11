# Class StandardWatchEventKinds

**Source:** `java.base\java\nio\file\StandardWatchEventKinds.html`

### Class Description

```java
public final class
StandardWatchEventKinds

extends
Object
```

Defines the

standard

event kinds.

**Since:** 1.7

---

### Field Details

#### public static final
WatchEvent.Kind
<
Object
> OVERFLOW

A special event to indicate that events may have been lost or
discarded.

The

context

for this event is
implementation specific and may be

null

. The event

count

may be greater than

1

.

**See Also:**
- WatchService

---

#### public static final
WatchEvent.Kind
<
Path
> ENTRY_CREATE

Directory entry created.

When a directory is registered for this event then the

WatchKey

is queued when it is observed that an entry is created in the directory
or renamed into the directory. The event

count

for this event is always

1

.

---

#### public static final
WatchEvent.Kind
<
Path
> ENTRY_DELETE

Directory entry deleted.

When a directory is registered for this event then the

WatchKey

is queued when it is observed that an entry is deleted or renamed out of
the directory. The event

count

for this event
is always

1

.

---

#### public static final
WatchEvent.Kind
<
Path
> ENTRY_MODIFY

Directory entry modified.

When a directory is registered for this event then the

WatchKey

is queued when it is observed that an entry in the directory has been
modified. The event

count

for this event is

1

or greater.

---

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Class StandardWatchEventKinds

java.lang.Object

- java.nio.file.StandardWatchEventKinds

java.nio.file.StandardWatchEventKinds

```java
public final class
StandardWatchEventKinds

extends
Object
```

Defines the

standard

event kinds.

**Since:** 1.7

public final class

StandardWatchEventKinds

extends

Object

Defines the

standard

event kinds.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

WatchEvent.Kind

<

Path

>

ENTRY_CREATE

Directory entry created.

static

WatchEvent.Kind

<

Path

>

ENTRY_DELETE

Directory entry deleted.

static

WatchEvent.Kind

<

Path

>

ENTRY_MODIFY

Directory entry modified.

static

WatchEvent.Kind

<

Object

>

OVERFLOW

A special event to indicate that events may have been lost or
discarded.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

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

WatchEvent.Kind

<

Path

>

ENTRY_CREATE

Directory entry created.

static

WatchEvent.Kind

<

Path

>

ENTRY_DELETE

Directory entry deleted.

static

WatchEvent.Kind

<

Path

>

ENTRY_MODIFY

Directory entry modified.

static

WatchEvent.Kind

<

Object

>

OVERFLOW

A special event to indicate that events may have been lost or
discarded.

---

#### Field Summary

Directory entry created.

Directory entry deleted.

Directory entry modified.

A special event to indicate that events may have been lost or
discarded.

Method Summary

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

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

- OVERFLOW

```java
public static final
WatchEvent.Kind
<
Object
> OVERFLOW
```

A special event to indicate that events may have been lost or
discarded.

The

context

for this event is
implementation specific and may be

null

. The event

count

may be greater than

1

.

**See Also:** WatchService

- ENTRY_CREATE

```java
public static final
WatchEvent.Kind
<
Path
> ENTRY_CREATE
```

Directory entry created.

When a directory is registered for this event then the

WatchKey

is queued when it is observed that an entry is created in the directory
or renamed into the directory. The event

count

for this event is always

1

.

- ENTRY_DELETE

```java
public static final
WatchEvent.Kind
<
Path
> ENTRY_DELETE
```

Directory entry deleted.

When a directory is registered for this event then the

WatchKey

is queued when it is observed that an entry is deleted or renamed out of
the directory. The event

count

for this event
is always

1

.

- ENTRY_MODIFY

```java
public static final
WatchEvent.Kind
<
Path
> ENTRY_MODIFY
```

Directory entry modified.

When a directory is registered for this event then the

WatchKey

is queued when it is observed that an entry in the directory has been
modified. The event

count

for this event is

1

or greater.

Field Detail

- OVERFLOW

```java
public static final
WatchEvent.Kind
<
Object
> OVERFLOW
```

A special event to indicate that events may have been lost or
discarded.

The

context

for this event is
implementation specific and may be

null

. The event

count

may be greater than

1

.

**See Also:** WatchService

- ENTRY_CREATE

```java
public static final
WatchEvent.Kind
<
Path
> ENTRY_CREATE
```

Directory entry created.

When a directory is registered for this event then the

WatchKey

is queued when it is observed that an entry is created in the directory
or renamed into the directory. The event

count

for this event is always

1

.

- ENTRY_DELETE

```java
public static final
WatchEvent.Kind
<
Path
> ENTRY_DELETE
```

Directory entry deleted.

When a directory is registered for this event then the

WatchKey

is queued when it is observed that an entry is deleted or renamed out of
the directory. The event

count

for this event
is always

1

.

- ENTRY_MODIFY

```java
public static final
WatchEvent.Kind
<
Path
> ENTRY_MODIFY
```

Directory entry modified.

When a directory is registered for this event then the

WatchKey

is queued when it is observed that an entry in the directory has been
modified. The event

count

for this event is

1

or greater.

---

#### Field Detail

OVERFLOW

```java
public static final
WatchEvent.Kind
<
Object
> OVERFLOW
```

A special event to indicate that events may have been lost or
discarded.

The

context

for this event is
implementation specific and may be

null

. The event

count

may be greater than

1

.

**See Also:** WatchService

---

#### OVERFLOW

public static final

WatchEvent.Kind

<

Object

> OVERFLOW

A special event to indicate that events may have been lost or
discarded.

The

context

for this event is
implementation specific and may be

null

. The event

count

may be greater than

1

.

The

context

for this event is
implementation specific and may be

null

. The event

count

may be greater than

1

.

ENTRY_CREATE

```java
public static final
WatchEvent.Kind
<
Path
> ENTRY_CREATE
```

Directory entry created.

When a directory is registered for this event then the

WatchKey

is queued when it is observed that an entry is created in the directory
or renamed into the directory. The event

count

for this event is always

1

.

---

#### ENTRY_CREATE

public static final

WatchEvent.Kind

<

Path

> ENTRY_CREATE

Directory entry created.

When a directory is registered for this event then the

WatchKey

is queued when it is observed that an entry is created in the directory
or renamed into the directory. The event

count

for this event is always

1

.

When a directory is registered for this event then the

WatchKey

is queued when it is observed that an entry is created in the directory
or renamed into the directory. The event

count

for this event is always

1

.

ENTRY_DELETE

```java
public static final
WatchEvent.Kind
<
Path
> ENTRY_DELETE
```

Directory entry deleted.

When a directory is registered for this event then the

WatchKey

is queued when it is observed that an entry is deleted or renamed out of
the directory. The event

count

for this event
is always

1

.

---

#### ENTRY_DELETE

public static final

WatchEvent.Kind

<

Path

> ENTRY_DELETE

Directory entry deleted.

When a directory is registered for this event then the

WatchKey

is queued when it is observed that an entry is deleted or renamed out of
the directory. The event

count

for this event
is always

1

.

When a directory is registered for this event then the

WatchKey

is queued when it is observed that an entry is deleted or renamed out of
the directory. The event

count

for this event
is always

1

.

ENTRY_MODIFY

```java
public static final
WatchEvent.Kind
<
Path
> ENTRY_MODIFY
```

Directory entry modified.

When a directory is registered for this event then the

WatchKey

is queued when it is observed that an entry in the directory has been
modified. The event

count

for this event is

1

or greater.

---

#### ENTRY_MODIFY

public static final

WatchEvent.Kind

<

Path

> ENTRY_MODIFY

Directory entry modified.

When a directory is registered for this event then the

WatchKey

is queued when it is observed that an entry in the directory has been
modified. The event

count

for this event is

1

or greater.

When a directory is registered for this event then the

WatchKey

is queued when it is observed that an entry in the directory has been
modified. The event

count

for this event is

1

or greater.

---

