# Class EventSettings

**Source:** `jdk.jfr\jdk\jfr\EventSettings.html`

### Class Description

```java
public abstract class
EventSettings

extends
Object
```

Convenience class for applying event settings to a recording.

An

EventSettings

object for a recording can be obtained by invoking
the

Recording.enable(String)

method which is configured using method
chaining.

The following example shows how to use the

EventSettings

class.

```java
Recording r = new Recording();
r.enable("jdk.CPULoad")
.withPeriod(Duration.ofSeconds(1));
r.enable("jdk.FileWrite")
.withoutStackTrace()
.withThreshold(Duration.ofNanos(10));
r.start();
Thread.sleep(10_000);
r.stop();
r.dump(Files.createTempFile("recording", ".jfr"));
```

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public final
EventSettings
withStackTrace()

Enables stack traces for the event that is associated with this event setting.

Equivalent to invoking the

with("stackTrace", "true")

method.

**Returns:**
- event settings object for further configuration, not

null

---

#### public final
EventSettings
withoutStackTrace()

Disables stack traces for the event that is associated with this event setting.

Equivalent to invoking the

with("stackTrace", "false")

method.

**Returns:**
- event settings object for further configuration, not

null

---

#### public final
EventSettings
withoutThreshold()

Specifies that a threshold is not used.

This is a convenience method, equivalent to invoking the

with("threshold", "0 s")

method.

**Returns:**
- event settings object for further configuration, not

null

---

#### public final
EventSettings
withPeriod​(
Duration
duration)

Sets the interval for the event that is associated with this event setting.

**Parameters:**
- duration

- the duration, not

null

**Returns:**
- event settings object for further configuration, not

null

---

#### public final
EventSettings
withThreshold​(
Duration
duration)

Sets the threshold for the event that is associated with this event setting.

**Parameters:**
- duration

- the duration, or

null

if no duration is used

**Returns:**
- event settings object for further configuration, not

null

---

#### public abstract
EventSettings
with​(
String
name,

String
value)

Sets a setting value for the event that is associated with this event setting.

**Parameters:**
- name

- the name of the setting (for example,

"threshold"

)
- value

- the value to set (for example

"20 ms"

not

null

)

**Returns:**
- event settings object for further configuration, not

null

---

### Additional Sections

#### Class EventSettings

java.lang.Object

- jdk.jfr.EventSettings

jdk.jfr.EventSettings

```java
public abstract class
EventSettings

extends
Object
```

Convenience class for applying event settings to a recording.

An

EventSettings

object for a recording can be obtained by invoking
the

Recording.enable(String)

method which is configured using method
chaining.

The following example shows how to use the

EventSettings

class.

```java
Recording r = new Recording();
r.enable("jdk.CPULoad")
.withPeriod(Duration.ofSeconds(1));
r.enable("jdk.FileWrite")
.withoutStackTrace()
.withThreshold(Duration.ofNanos(10));
r.start();
Thread.sleep(10_000);
r.stop();
r.dump(Files.createTempFile("recording", ".jfr"));
```

**Since:** 9

public abstract class

EventSettings

extends

Object

Convenience class for applying event settings to a recording.

An

EventSettings

object for a recording can be obtained by invoking
the

Recording.enable(String)

method which is configured using method
chaining.

The following example shows how to use the

EventSettings

class.

```java
Recording r = new Recording();
r.enable("jdk.CPULoad")
.withPeriod(Duration.ofSeconds(1));
r.enable("jdk.FileWrite")
.withoutStackTrace()
.withThreshold(Duration.ofNanos(10));
r.start();
Thread.sleep(10_000);
r.stop();
r.dump(Files.createTempFile("recording", ".jfr"));
```

An

EventSettings

object for a recording can be obtained by invoking
the

Recording.enable(String)

method which is configured using method
chaining.

The following example shows how to use the

EventSettings

class.

```java
Recording r = new Recording();
r.enable("jdk.CPULoad")
.withPeriod(Duration.ofSeconds(1));
r.enable("jdk.FileWrite")
.withoutStackTrace()
.withThreshold(Duration.ofNanos(10));
r.start();
Thread.sleep(10_000);
r.stop();
r.dump(Files.createTempFile("recording", ".jfr"));
```

The following example shows how to use the

EventSettings

class.

```java
Recording r = new Recording();
r.enable("jdk.CPULoad")
.withPeriod(Duration.ofSeconds(1));
r.enable("jdk.FileWrite")
.withoutStackTrace()
.withThreshold(Duration.ofNanos(10));
r.start();
Thread.sleep(10_000);
r.stop();
r.dump(Files.createTempFile("recording", ".jfr"));
```

Recording r = new Recording();
r.enable("jdk.CPULoad")
.withPeriod(Duration.ofSeconds(1));
r.enable("jdk.FileWrite")
.withoutStackTrace()
.withThreshold(Duration.ofNanos(10));
r.start();
Thread.sleep(10_000);
r.stop();
r.dump(Files.createTempFile("recording", ".jfr"));

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

EventSettings

with

​(

String

name,

String

value)

Sets a setting value for the event that is associated with this event setting.

EventSettings

withoutStackTrace

()

Disables stack traces for the event that is associated with this event setting.

EventSettings

withoutThreshold

()

Specifies that a threshold is not used.

EventSettings

withPeriod

​(

Duration

duration)

Sets the interval for the event that is associated with this event setting.

EventSettings

withStackTrace

()

Enables stack traces for the event that is associated with this event setting.

EventSettings

withThreshold

​(

Duration

duration)

Sets the threshold for the event that is associated with this event setting.

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

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

EventSettings

with

​(

String

name,

String

value)

Sets a setting value for the event that is associated with this event setting.

EventSettings

withoutStackTrace

()

Disables stack traces for the event that is associated with this event setting.

EventSettings

withoutThreshold

()

Specifies that a threshold is not used.

EventSettings

withPeriod

​(

Duration

duration)

Sets the interval for the event that is associated with this event setting.

EventSettings

withStackTrace

()

Enables stack traces for the event that is associated with this event setting.

EventSettings

withThreshold

​(

Duration

duration)

Sets the threshold for the event that is associated with this event setting.

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

Sets a setting value for the event that is associated with this event setting.

Disables stack traces for the event that is associated with this event setting.

Specifies that a threshold is not used.

Sets the interval for the event that is associated with this event setting.

Enables stack traces for the event that is associated with this event setting.

Sets the threshold for the event that is associated with this event setting.

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

============ METHOD DETAIL ==========

- Method Detail

- withStackTrace

```java
public final
EventSettings
withStackTrace()
```

Enables stack traces for the event that is associated with this event setting.

Equivalent to invoking the

with("stackTrace", "true")

method.

**Returns:** event settings object for further configuration, not

null

- withoutStackTrace

```java
public final
EventSettings
withoutStackTrace()
```

Disables stack traces for the event that is associated with this event setting.

Equivalent to invoking the

with("stackTrace", "false")

method.

**Returns:** event settings object for further configuration, not

null

- withoutThreshold

```java
public final
EventSettings
withoutThreshold()
```

Specifies that a threshold is not used.

This is a convenience method, equivalent to invoking the

with("threshold", "0 s")

method.

**Returns:** event settings object for further configuration, not

null

- withPeriod

```java
public final
EventSettings
withPeriod​(
Duration
duration)
```

Sets the interval for the event that is associated with this event setting.

**Parameters:** duration

- the duration, not

null
**Returns:** event settings object for further configuration, not

null

- withThreshold

```java
public final
EventSettings
withThreshold​(
Duration
duration)
```

Sets the threshold for the event that is associated with this event setting.

**Parameters:** duration

- the duration, or

null

if no duration is used
**Returns:** event settings object for further configuration, not

null

- with

```java
public abstract
EventSettings
with​(
String
name,

String
value)
```

Sets a setting value for the event that is associated with this event setting.

**Parameters:** name

- the name of the setting (for example,

"threshold"

)
**Parameters:** value

- the value to set (for example

"20 ms"

not

null

)
**Returns:** event settings object for further configuration, not

null

Method Detail

- withStackTrace

```java
public final
EventSettings
withStackTrace()
```

Enables stack traces for the event that is associated with this event setting.

Equivalent to invoking the

with("stackTrace", "true")

method.

**Returns:** event settings object for further configuration, not

null

- withoutStackTrace

```java
public final
EventSettings
withoutStackTrace()
```

Disables stack traces for the event that is associated with this event setting.

Equivalent to invoking the

with("stackTrace", "false")

method.

**Returns:** event settings object for further configuration, not

null

- withoutThreshold

```java
public final
EventSettings
withoutThreshold()
```

Specifies that a threshold is not used.

This is a convenience method, equivalent to invoking the

with("threshold", "0 s")

method.

**Returns:** event settings object for further configuration, not

null

- withPeriod

```java
public final
EventSettings
withPeriod​(
Duration
duration)
```

Sets the interval for the event that is associated with this event setting.

**Parameters:** duration

- the duration, not

null
**Returns:** event settings object for further configuration, not

null

- withThreshold

```java
public final
EventSettings
withThreshold​(
Duration
duration)
```

Sets the threshold for the event that is associated with this event setting.

**Parameters:** duration

- the duration, or

null

if no duration is used
**Returns:** event settings object for further configuration, not

null

- with

```java
public abstract
EventSettings
with​(
String
name,

String
value)
```

Sets a setting value for the event that is associated with this event setting.

**Parameters:** name

- the name of the setting (for example,

"threshold"

)
**Parameters:** value

- the value to set (for example

"20 ms"

not

null

)
**Returns:** event settings object for further configuration, not

null

---

#### Method Detail

withStackTrace

```java
public final
EventSettings
withStackTrace()
```

Enables stack traces for the event that is associated with this event setting.

Equivalent to invoking the

with("stackTrace", "true")

method.

**Returns:** event settings object for further configuration, not

null

---

#### withStackTrace

public final

EventSettings

withStackTrace()

Enables stack traces for the event that is associated with this event setting.

Equivalent to invoking the

with("stackTrace", "true")

method.

Equivalent to invoking the

with("stackTrace", "true")

method.

withoutStackTrace

```java
public final
EventSettings
withoutStackTrace()
```

Disables stack traces for the event that is associated with this event setting.

Equivalent to invoking the

with("stackTrace", "false")

method.

**Returns:** event settings object for further configuration, not

null

---

#### withoutStackTrace

public final

EventSettings

withoutStackTrace()

Disables stack traces for the event that is associated with this event setting.

Equivalent to invoking the

with("stackTrace", "false")

method.

Equivalent to invoking the

with("stackTrace", "false")

method.

withoutThreshold

```java
public final
EventSettings
withoutThreshold()
```

Specifies that a threshold is not used.

This is a convenience method, equivalent to invoking the

with("threshold", "0 s")

method.

**Returns:** event settings object for further configuration, not

null

---

#### withoutThreshold

public final

EventSettings

withoutThreshold()

Specifies that a threshold is not used.

This is a convenience method, equivalent to invoking the

with("threshold", "0 s")

method.

This is a convenience method, equivalent to invoking the

with("threshold", "0 s")

method.

withPeriod

```java
public final
EventSettings
withPeriod​(
Duration
duration)
```

Sets the interval for the event that is associated with this event setting.

**Parameters:** duration

- the duration, not

null
**Returns:** event settings object for further configuration, not

null

---

#### withPeriod

public final

EventSettings

withPeriod​(

Duration

duration)

Sets the interval for the event that is associated with this event setting.

withThreshold

```java
public final
EventSettings
withThreshold​(
Duration
duration)
```

Sets the threshold for the event that is associated with this event setting.

**Parameters:** duration

- the duration, or

null

if no duration is used
**Returns:** event settings object for further configuration, not

null

---

#### withThreshold

public final

EventSettings

withThreshold​(

Duration

duration)

Sets the threshold for the event that is associated with this event setting.

with

```java
public abstract
EventSettings
with​(
String
name,

String
value)
```

Sets a setting value for the event that is associated with this event setting.

**Parameters:** name

- the name of the setting (for example,

"threshold"

)
**Parameters:** value

- the value to set (for example

"20 ms"

not

null

)
**Returns:** event settings object for further configuration, not

null

---

#### with

public abstract

EventSettings

with​(

String

name,

String

value)

Sets a setting value for the event that is associated with this event setting.

---

