# Interface Delayed

**Source:** `java.base\java\util\concurrent\Delayed.html`

### Class Description

```java
public interface
Delayed

extends
Comparable
<
Delayed
>
```

A mix-in style interface for marking objects that should be
acted upon after a given delay.

An implementation of this interface must define a

compareTo

method that provides an ordering consistent with
its

getDelay

method.

**All Superinterfaces:** Comparable

<

Delayed

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### long getDelay​(
TimeUnit
unit)

Returns the remaining delay associated with this object, in the
given time unit.

**Parameters:**
- unit

- the time unit

**Returns:**
- the remaining delay; zero or negative values indicate
that the delay has already elapsed

---

### Additional Sections

#### Interface Delayed

**All Superinterfaces:** Comparable

<

Delayed

>

**All Known Subinterfaces:** RunnableScheduledFuture

<V>

,

ScheduledFuture

<V>

```java
public interface
Delayed

extends
Comparable
<
Delayed
>
```

A mix-in style interface for marking objects that should be
acted upon after a given delay.

An implementation of this interface must define a

compareTo

method that provides an ordering consistent with
its

getDelay

method.

**Since:** 1.5

public interface

Delayed

extends

Comparable

<

Delayed

>

A mix-in style interface for marking objects that should be
acted upon after a given delay.

An implementation of this interface must define a

compareTo

method that provides an ordering consistent with
its

getDelay

method.

An implementation of this interface must define a

compareTo

method that provides an ordering consistent with
its

getDelay

method.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

long

getDelay

​(

TimeUnit

unit)

Returns the remaining delay associated with this object, in the
given time unit.

- Methods declared in interface java.lang.

Comparable

compareTo

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

long

getDelay

​(

TimeUnit

unit)

Returns the remaining delay associated with this object, in the
given time unit.

- Methods declared in interface java.lang.

Comparable

compareTo

---

#### Method Summary

Returns the remaining delay associated with this object, in the
given time unit.

Methods declared in interface java.lang.

Comparable

compareTo

---

#### Methods declared in interface java.lang. Comparable

============ METHOD DETAIL ==========

- Method Detail

- getDelay

```java
long getDelay​(
TimeUnit
unit)
```

Returns the remaining delay associated with this object, in the
given time unit.

**Parameters:** unit

- the time unit
**Returns:** the remaining delay; zero or negative values indicate
that the delay has already elapsed

Method Detail

- getDelay

```java
long getDelay​(
TimeUnit
unit)
```

Returns the remaining delay associated with this object, in the
given time unit.

**Parameters:** unit

- the time unit
**Returns:** the remaining delay; zero or negative values indicate
that the delay has already elapsed

---

#### Method Detail

getDelay

```java
long getDelay​(
TimeUnit
unit)
```

Returns the remaining delay associated with this object, in the
given time unit.

**Parameters:** unit

- the time unit
**Returns:** the remaining delay; zero or negative values indicate
that the delay has already elapsed

---

#### getDelay

long getDelay​(

TimeUnit

unit)

Returns the remaining delay associated with this object, in the
given time unit.

---

