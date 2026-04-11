# Class FlightRecorderPermission

**Source:** `jdk.jfr\jdk\jfr\FlightRecorderPermission.html`

### Class Description

```java
public final class
FlightRecorderPermission

extends
BasicPermission
```

Permission for controlling access to Flight Recorder.

The following table provides a summary of what the permission
allows, and the risks of granting code the permission.

Table shows permission target name,
what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

accessFlightRecorder

Ability to create a Flight Recorder instance, register callbacks to
monitor the Flight Recorder life cycle, and control an existing instance
of Flight Recorder, which can record and dump runtime information, such as
stack traces, class names, and data in user defined events.

A malicious user may be able to extract sensitive information that is stored in
events and interrupt Flight Recorder by installing listeners or hooks that
never finish.

registerEvent

Ability to register events, write data to the Flight Recorder buffers,
and execute code in a callback function for periodic events.

A malicious user may be able to write sensitive information to Flight
Recorder buffers.

Typically, programmers do not create

FlightRecorderPermission

objects
directly. Instead the objects are created by the security policy code that is based on
reading the security policy file.

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public FlightRecorderPermission​(
String
name)

Constructs a

FlightRecorderPermission

with the specified name.

**Parameters:**
- name

- the permission name, must be either

"accessFlightRecorder"

or

"registerEvent"

, not

null

**Throws:**
- IllegalArgumentException

- if

name

is empty or not valid

---

### Method Details

*No entries found.*

### Additional Sections

#### Class FlightRecorderPermission

java.lang.Object

- java.security.Permission
- - java.security.BasicPermission
- - jdk.jfr.FlightRecorderPermission

java.security.Permission

- java.security.BasicPermission
- - jdk.jfr.FlightRecorderPermission

java.security.BasicPermission

- jdk.jfr.FlightRecorderPermission

jdk.jfr.FlightRecorderPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public final class
FlightRecorderPermission

extends
BasicPermission
```

Permission for controlling access to Flight Recorder.

The following table provides a summary of what the permission
allows, and the risks of granting code the permission.

Table shows permission target name,
what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

accessFlightRecorder

Ability to create a Flight Recorder instance, register callbacks to
monitor the Flight Recorder life cycle, and control an existing instance
of Flight Recorder, which can record and dump runtime information, such as
stack traces, class names, and data in user defined events.

A malicious user may be able to extract sensitive information that is stored in
events and interrupt Flight Recorder by installing listeners or hooks that
never finish.

registerEvent

Ability to register events, write data to the Flight Recorder buffers,
and execute code in a callback function for periodic events.

A malicious user may be able to write sensitive information to Flight
Recorder buffers.

Typically, programmers do not create

FlightRecorderPermission

objects
directly. Instead the objects are created by the security policy code that is based on
reading the security policy file.

**Since:** 9
**See Also:** BasicPermission

,

Permission

,

Permissions

,

PermissionCollection

,

SecurityManager

,

Serialized Form

public final class

FlightRecorderPermission

extends

BasicPermission

Permission for controlling access to Flight Recorder.

The following table provides a summary of what the permission
allows, and the risks of granting code the permission.

Table shows permission target name,
what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

accessFlightRecorder

Ability to create a Flight Recorder instance, register callbacks to
monitor the Flight Recorder life cycle, and control an existing instance
of Flight Recorder, which can record and dump runtime information, such as
stack traces, class names, and data in user defined events.

A malicious user may be able to extract sensitive information that is stored in
events and interrupt Flight Recorder by installing listeners or hooks that
never finish.

registerEvent

Ability to register events, write data to the Flight Recorder buffers,
and execute code in a callback function for periodic events.

A malicious user may be able to write sensitive information to Flight
Recorder buffers.

Typically, programmers do not create

FlightRecorderPermission

objects
directly. Instead the objects are created by the security policy code that is based on
reading the security policy file.

The following table provides a summary of what the permission
allows, and the risks of granting code the permission.

Table shows permission target name,
what the permission allows, and associated risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

accessFlightRecorder

Ability to create a Flight Recorder instance, register callbacks to
monitor the Flight Recorder life cycle, and control an existing instance
of Flight Recorder, which can record and dump runtime information, such as
stack traces, class names, and data in user defined events.

A malicious user may be able to extract sensitive information that is stored in
events and interrupt Flight Recorder by installing listeners or hooks that
never finish.

registerEvent

Ability to register events, write data to the Flight Recorder buffers,
and execute code in a callback function for periodic events.

A malicious user may be able to write sensitive information to Flight
Recorder buffers.

Typically, programmers do not create

FlightRecorderPermission

objects
directly. Instead the objects are created by the security policy code that is based on
reading the security policy file.

Typically, programmers do not create

FlightRecorderPermission

objects
directly. Instead the objects are created by the security policy code that is based on
reading the security policy file.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FlightRecorderPermission

​(

String

name)

Constructs a

FlightRecorderPermission

with the specified name.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.security.

BasicPermission

equals

,

getActions

,

hashCode

,

implies

,

newPermissionCollection

- Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

FlightRecorderPermission

​(

String

name)

Constructs a

FlightRecorderPermission

with the specified name.

---

#### Constructor Summary

Constructs a

FlightRecorderPermission

with the specified name.

Method Summary

- Methods declared in class java.security.

BasicPermission

equals

,

getActions

,

hashCode

,

implies

,

newPermissionCollection

- Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Methods declared in class java.security.

BasicPermission

equals

,

getActions

,

hashCode

,

implies

,

newPermissionCollection

---

#### Methods declared in class java.security. BasicPermission

Methods declared in class java.security.

Permission

checkGuard

,

getName

,

toString

---

#### Methods declared in class java.security. Permission

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- FlightRecorderPermission

```java
public FlightRecorderPermission​(
String
name)
```

Constructs a

FlightRecorderPermission

with the specified name.

**Parameters:** name

- the permission name, must be either

"accessFlightRecorder"

or

"registerEvent"

, not

null
**Throws:** IllegalArgumentException

- if

name

is empty or not valid

Constructor Detail

- FlightRecorderPermission

```java
public FlightRecorderPermission​(
String
name)
```

Constructs a

FlightRecorderPermission

with the specified name.

**Parameters:** name

- the permission name, must be either

"accessFlightRecorder"

or

"registerEvent"

, not

null
**Throws:** IllegalArgumentException

- if

name

is empty or not valid

---

#### Constructor Detail

FlightRecorderPermission

```java
public FlightRecorderPermission​(
String
name)
```

Constructs a

FlightRecorderPermission

with the specified name.

**Parameters:** name

- the permission name, must be either

"accessFlightRecorder"

or

"registerEvent"

, not

null
**Throws:** IllegalArgumentException

- if

name

is empty or not valid

---

#### FlightRecorderPermission

public FlightRecorderPermission​(

String

name)

Constructs a

FlightRecorderPermission

with the specified name.

---

