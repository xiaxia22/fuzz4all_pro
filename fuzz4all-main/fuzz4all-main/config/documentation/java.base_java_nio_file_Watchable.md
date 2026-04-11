# Interface Watchable

**Source:** `java.base\java\nio\file\Watchable.html`

### Class Description

```java
public interface
Watchable
```

An object that may be registered with a watch service so that it can be

watched

for changes and events.

This interface defines the

register

method to register
the object with a

WatchService

returning a

WatchKey

to
represent the registration. An object may be registered with more than one
watch service. Registration with a watch service is cancelled by invoking the
key's

cancel

method.

**All Known Subinterfaces:** Path

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### WatchKey
register​(
WatchService
watcher,

WatchEvent.Kind
<?>[] events,

WatchEvent.Modifier
... modifiers)
throws
IOException

Registers an object with a watch service.

If the file system object identified by this object is currently
registered with the watch service then the watch key, representing that
registration, is returned after changing the event set or modifiers to
those specified by the

events

and

modifiers

parameters.
Changing the event set does not cause pending events for the object to be
discarded. Objects are automatically registered for the

OVERFLOW

event. This event is not
required to be present in the array of events.

Otherwise the file system object has not yet been registered with the
given watch service, so it is registered and the resulting new key is
returned.

Implementations of this interface should specify the events they
support.

**Parameters:**
- watcher

- the watch service to which this object is to be registered
- events

- the events for which this object should be registered
- modifiers

- the modifiers, if any, that modify how the object is registered

**Returns:**
- a key representing the registration of this object with the
given watch service

**Throws:**
- UnsupportedOperationException

- if unsupported events or modifiers are specified
- IllegalArgumentException

- if an invalid of combination of events are modifiers are specified
- ClosedWatchServiceException

- if the watch service is closed
- IOException

- if an I/O error occurs
- SecurityException

- if a security manager is installed and it denies an unspecified
permission required to monitor this object. Implementations of
this interface should specify the permission checks.

---

#### WatchKey
register​(
WatchService
watcher,

WatchEvent.Kind
<?>... events)
throws
IOException

Registers an object with a watch service.

An invocation of this method behaves in exactly the same way as the
invocation

```java
watchable.
register
(watcher, events, new WatchEvent.Modifier[0]);
```

**Parameters:**
- watcher

- the watch service to which this object is to be registered
- events

- the events for which this object should be registered

**Returns:**
- a key representing the registration of this object with the
given watch service

**Throws:**
- UnsupportedOperationException

- if unsupported events are specified
- IllegalArgumentException

- if an invalid of combination of events are specified
- ClosedWatchServiceException

- if the watch service is closed
- IOException

- if an I/O error occurs
- SecurityException

- if a security manager is installed and it denies an unspecified
permission required to monitor this object. Implementations of
this interface should specify the permission checks.

---

### Additional Sections

#### Interface Watchable

**All Known Subinterfaces:** Path

```java
public interface
Watchable
```

An object that may be registered with a watch service so that it can be

watched

for changes and events.

This interface defines the

register

method to register
the object with a

WatchService

returning a

WatchKey

to
represent the registration. An object may be registered with more than one
watch service. Registration with a watch service is cancelled by invoking the
key's

cancel

method.

**Since:** 1.7
**See Also:** Path.register(java.nio.file.WatchService, java.nio.file.WatchEvent.Kind<?>[], java.nio.file.WatchEvent.Modifier...)

public interface

Watchable

An object that may be registered with a watch service so that it can be

watched

for changes and events.

This interface defines the

register

method to register
the object with a

WatchService

returning a

WatchKey

to
represent the registration. An object may be registered with more than one
watch service. Registration with a watch service is cancelled by invoking the
key's

cancel

method.

This interface defines the

register

method to register
the object with a

WatchService

returning a

WatchKey

to
represent the registration. An object may be registered with more than one
watch service. Registration with a watch service is cancelled by invoking the
key's

cancel

method.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

WatchKey

register

​(

WatchService

watcher,

WatchEvent.Kind

<?>... events)

Registers an object with a watch service.

WatchKey

register

​(

WatchService

watcher,

WatchEvent.Kind

<?>[] events,

WatchEvent.Modifier

... modifiers)

Registers an object with a watch service.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

WatchKey

register

​(

WatchService

watcher,

WatchEvent.Kind

<?>... events)

Registers an object with a watch service.

WatchKey

register

​(

WatchService

watcher,

WatchEvent.Kind

<?>[] events,

WatchEvent.Modifier

... modifiers)

Registers an object with a watch service.

---

#### Method Summary

Registers an object with a watch service.

============ METHOD DETAIL ==========

- Method Detail

- register

```java
WatchKey
register​(
WatchService
watcher,

WatchEvent.Kind
<?>[] events,

WatchEvent.Modifier
... modifiers)
throws
IOException
```

Registers an object with a watch service.

If the file system object identified by this object is currently
registered with the watch service then the watch key, representing that
registration, is returned after changing the event set or modifiers to
those specified by the

events

and

modifiers

parameters.
Changing the event set does not cause pending events for the object to be
discarded. Objects are automatically registered for the

OVERFLOW

event. This event is not
required to be present in the array of events.

Otherwise the file system object has not yet been registered with the
given watch service, so it is registered and the resulting new key is
returned.

Implementations of this interface should specify the events they
support.

**Parameters:** watcher

- the watch service to which this object is to be registered
**Parameters:** events

- the events for which this object should be registered
**Parameters:** modifiers

- the modifiers, if any, that modify how the object is registered
**Returns:** a key representing the registration of this object with the
given watch service
**Throws:** UnsupportedOperationException

- if unsupported events or modifiers are specified
**Throws:** IllegalArgumentException

- if an invalid of combination of events are modifiers are specified
**Throws:** ClosedWatchServiceException

- if the watch service is closed
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- if a security manager is installed and it denies an unspecified
permission required to monitor this object. Implementations of
this interface should specify the permission checks.

- register

```java
WatchKey
register​(
WatchService
watcher,

WatchEvent.Kind
<?>... events)
throws
IOException
```

Registers an object with a watch service.

An invocation of this method behaves in exactly the same way as the
invocation

```java
watchable.
register
(watcher, events, new WatchEvent.Modifier[0]);
```

**Parameters:** watcher

- the watch service to which this object is to be registered
**Parameters:** events

- the events for which this object should be registered
**Returns:** a key representing the registration of this object with the
given watch service
**Throws:** UnsupportedOperationException

- if unsupported events are specified
**Throws:** IllegalArgumentException

- if an invalid of combination of events are specified
**Throws:** ClosedWatchServiceException

- if the watch service is closed
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- if a security manager is installed and it denies an unspecified
permission required to monitor this object. Implementations of
this interface should specify the permission checks.

Method Detail

- register

```java
WatchKey
register​(
WatchService
watcher,

WatchEvent.Kind
<?>[] events,

WatchEvent.Modifier
... modifiers)
throws
IOException
```

Registers an object with a watch service.

If the file system object identified by this object is currently
registered with the watch service then the watch key, representing that
registration, is returned after changing the event set or modifiers to
those specified by the

events

and

modifiers

parameters.
Changing the event set does not cause pending events for the object to be
discarded. Objects are automatically registered for the

OVERFLOW

event. This event is not
required to be present in the array of events.

Otherwise the file system object has not yet been registered with the
given watch service, so it is registered and the resulting new key is
returned.

Implementations of this interface should specify the events they
support.

**Parameters:** watcher

- the watch service to which this object is to be registered
**Parameters:** events

- the events for which this object should be registered
**Parameters:** modifiers

- the modifiers, if any, that modify how the object is registered
**Returns:** a key representing the registration of this object with the
given watch service
**Throws:** UnsupportedOperationException

- if unsupported events or modifiers are specified
**Throws:** IllegalArgumentException

- if an invalid of combination of events are modifiers are specified
**Throws:** ClosedWatchServiceException

- if the watch service is closed
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- if a security manager is installed and it denies an unspecified
permission required to monitor this object. Implementations of
this interface should specify the permission checks.

- register

```java
WatchKey
register​(
WatchService
watcher,

WatchEvent.Kind
<?>... events)
throws
IOException
```

Registers an object with a watch service.

An invocation of this method behaves in exactly the same way as the
invocation

```java
watchable.
register
(watcher, events, new WatchEvent.Modifier[0]);
```

**Parameters:** watcher

- the watch service to which this object is to be registered
**Parameters:** events

- the events for which this object should be registered
**Returns:** a key representing the registration of this object with the
given watch service
**Throws:** UnsupportedOperationException

- if unsupported events are specified
**Throws:** IllegalArgumentException

- if an invalid of combination of events are specified
**Throws:** ClosedWatchServiceException

- if the watch service is closed
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- if a security manager is installed and it denies an unspecified
permission required to monitor this object. Implementations of
this interface should specify the permission checks.

---

#### Method Detail

register

```java
WatchKey
register​(
WatchService
watcher,

WatchEvent.Kind
<?>[] events,

WatchEvent.Modifier
... modifiers)
throws
IOException
```

Registers an object with a watch service.

If the file system object identified by this object is currently
registered with the watch service then the watch key, representing that
registration, is returned after changing the event set or modifiers to
those specified by the

events

and

modifiers

parameters.
Changing the event set does not cause pending events for the object to be
discarded. Objects are automatically registered for the

OVERFLOW

event. This event is not
required to be present in the array of events.

Otherwise the file system object has not yet been registered with the
given watch service, so it is registered and the resulting new key is
returned.

Implementations of this interface should specify the events they
support.

**Parameters:** watcher

- the watch service to which this object is to be registered
**Parameters:** events

- the events for which this object should be registered
**Parameters:** modifiers

- the modifiers, if any, that modify how the object is registered
**Returns:** a key representing the registration of this object with the
given watch service
**Throws:** UnsupportedOperationException

- if unsupported events or modifiers are specified
**Throws:** IllegalArgumentException

- if an invalid of combination of events are modifiers are specified
**Throws:** ClosedWatchServiceException

- if the watch service is closed
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- if a security manager is installed and it denies an unspecified
permission required to monitor this object. Implementations of
this interface should specify the permission checks.

---

#### register

WatchKey

register​(

WatchService

watcher,

WatchEvent.Kind

<?>[] events,

WatchEvent.Modifier

... modifiers)
throws

IOException

Registers an object with a watch service.

If the file system object identified by this object is currently
registered with the watch service then the watch key, representing that
registration, is returned after changing the event set or modifiers to
those specified by the

events

and

modifiers

parameters.
Changing the event set does not cause pending events for the object to be
discarded. Objects are automatically registered for the

OVERFLOW

event. This event is not
required to be present in the array of events.

Otherwise the file system object has not yet been registered with the
given watch service, so it is registered and the resulting new key is
returned.

Implementations of this interface should specify the events they
support.

If the file system object identified by this object is currently
registered with the watch service then the watch key, representing that
registration, is returned after changing the event set or modifiers to
those specified by the

events

and

modifiers

parameters.
Changing the event set does not cause pending events for the object to be
discarded. Objects are automatically registered for the

OVERFLOW

event. This event is not
required to be present in the array of events.

Otherwise the file system object has not yet been registered with the
given watch service, so it is registered and the resulting new key is
returned.

Implementations of this interface should specify the events they
support.

Otherwise the file system object has not yet been registered with the
given watch service, so it is registered and the resulting new key is
returned.

Implementations of this interface should specify the events they
support.

Implementations of this interface should specify the events they
support.

register

```java
WatchKey
register​(
WatchService
watcher,

WatchEvent.Kind
<?>... events)
throws
IOException
```

Registers an object with a watch service.

An invocation of this method behaves in exactly the same way as the
invocation

```java
watchable.
register
(watcher, events, new WatchEvent.Modifier[0]);
```

**Parameters:** watcher

- the watch service to which this object is to be registered
**Parameters:** events

- the events for which this object should be registered
**Returns:** a key representing the registration of this object with the
given watch service
**Throws:** UnsupportedOperationException

- if unsupported events are specified
**Throws:** IllegalArgumentException

- if an invalid of combination of events are specified
**Throws:** ClosedWatchServiceException

- if the watch service is closed
**Throws:** IOException

- if an I/O error occurs
**Throws:** SecurityException

- if a security manager is installed and it denies an unspecified
permission required to monitor this object. Implementations of
this interface should specify the permission checks.

---

#### register

WatchKey

register​(

WatchService

watcher,

WatchEvent.Kind

<?>... events)
throws

IOException

Registers an object with a watch service.

An invocation of this method behaves in exactly the same way as the
invocation

```java
watchable.
register
(watcher, events, new WatchEvent.Modifier[0]);
```

An invocation of this method behaves in exactly the same way as the
invocation

```java
watchable.
register
(watcher, events, new WatchEvent.Modifier[0]);
```

watchable.

register

(watcher, events, new WatchEvent.Modifier[0]);

---

