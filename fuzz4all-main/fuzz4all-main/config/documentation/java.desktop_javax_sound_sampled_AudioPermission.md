# Class AudioPermission

**Source:** `java.desktop\javax\sound\sampled\AudioPermission.html`

### Class Description

```java
public class
AudioPermission

extends
BasicPermission
```

The

AudioPermission

class represents access rights to the audio
system resources. An

AudioPermission

contains a target name but no
actions list; you either have the named permission or you don't.

The target name is the name of the audio permission (see the table below).
The names follow the hierarchical property-naming convention. Also, an
asterisk can be used to represent all the audio permissions.

The following table lists the possible

AudioPermission

target names.
For each name, the table provides a description of exactly what that
permission allows, as well as a discussion of the risks of granting code the
permission.

Permission target name, what the permission allows, and associated
risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

play

Audio playback through the audio device or devices on the system.
Allows the application to obtain and manipulate lines and mixers for
audio playback (rendering).

In some cases use of this permission may affect other
applications because the audio from one line may be mixed with other
audio being played on the system, or because manipulation of a mixer
affects the audio for all lines using that mixer.

record

Audio recording through the audio device or devices on the system.
Allows the application to obtain and manipulate lines and mixers for
audio recording (capture).

In some cases use of this permission may affect other applications
because manipulation of a mixer affects the audio for all lines using
that mixer. This permission can enable an applet or application to
eavesdrop on a user.

**All Implemented Interfaces:** Serializable

,

Guard

---

### Field Details

*No entries found.*

### Constructor Details

#### public AudioPermission​(
String
name)

Creates a new

AudioPermission

object that has the specified
symbolic name, such as "play" or "record". An asterisk can be used to
indicate all audio permissions.

**Parameters:**
- name

- the name of the new

AudioPermission

**Throws:**
- NullPointerException

- if

name

is

null
- IllegalArgumentException

- if

name

is empty

---

#### public AudioPermission​(
String
name,

String
actions)

Creates a new

AudioPermission

object that has the specified
symbolic name, such as "play" or "record". The

actions

parameter
is currently unused and should be

null

.

**Parameters:**
- name

- the name of the new

AudioPermission
- actions

- (unused; should be

null

)

**Throws:**
- NullPointerException

- if

name

is

null
- IllegalArgumentException

- if

name

is empty

---

### Method Details

*No entries found.*

### Additional Sections

#### Class AudioPermission

java.lang.Object

- java.security.Permission
- - java.security.BasicPermission
- - javax.sound.sampled.AudioPermission

java.security.Permission

- java.security.BasicPermission
- - javax.sound.sampled.AudioPermission

java.security.BasicPermission

- javax.sound.sampled.AudioPermission

javax.sound.sampled.AudioPermission

**All Implemented Interfaces:** Serializable

,

Guard

```java
public class
AudioPermission

extends
BasicPermission
```

The

AudioPermission

class represents access rights to the audio
system resources. An

AudioPermission

contains a target name but no
actions list; you either have the named permission or you don't.

The target name is the name of the audio permission (see the table below).
The names follow the hierarchical property-naming convention. Also, an
asterisk can be used to represent all the audio permissions.

The following table lists the possible

AudioPermission

target names.
For each name, the table provides a description of exactly what that
permission allows, as well as a discussion of the risks of granting code the
permission.

Permission target name, what the permission allows, and associated
risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

play

Audio playback through the audio device or devices on the system.
Allows the application to obtain and manipulate lines and mixers for
audio playback (rendering).

In some cases use of this permission may affect other
applications because the audio from one line may be mixed with other
audio being played on the system, or because manipulation of a mixer
affects the audio for all lines using that mixer.

record

Audio recording through the audio device or devices on the system.
Allows the application to obtain and manipulate lines and mixers for
audio recording (capture).

In some cases use of this permission may affect other applications
because manipulation of a mixer affects the audio for all lines using
that mixer. This permission can enable an applet or application to
eavesdrop on a user.

**Since:** 1.3
**See Also:** Serialized Form

public class

AudioPermission

extends

BasicPermission

The

AudioPermission

class represents access rights to the audio
system resources. An

AudioPermission

contains a target name but no
actions list; you either have the named permission or you don't.

The target name is the name of the audio permission (see the table below).
The names follow the hierarchical property-naming convention. Also, an
asterisk can be used to represent all the audio permissions.

The following table lists the possible

AudioPermission

target names.
For each name, the table provides a description of exactly what that
permission allows, as well as a discussion of the risks of granting code the
permission.

Permission target name, what the permission allows, and associated
risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

play

Audio playback through the audio device or devices on the system.
Allows the application to obtain and manipulate lines and mixers for
audio playback (rendering).

In some cases use of this permission may affect other
applications because the audio from one line may be mixed with other
audio being played on the system, or because manipulation of a mixer
affects the audio for all lines using that mixer.

record

Audio recording through the audio device or devices on the system.
Allows the application to obtain and manipulate lines and mixers for
audio recording (capture).

In some cases use of this permission may affect other applications
because manipulation of a mixer affects the audio for all lines using
that mixer. This permission can enable an applet or application to
eavesdrop on a user.

The target name is the name of the audio permission (see the table below).
The names follow the hierarchical property-naming convention. Also, an
asterisk can be used to represent all the audio permissions.

The following table lists the possible

AudioPermission

target names.
For each name, the table provides a description of exactly what that
permission allows, as well as a discussion of the risks of granting code the
permission.

Permission target name, what the permission allows, and associated
risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

play

Audio playback through the audio device or devices on the system.
Allows the application to obtain and manipulate lines and mixers for
audio playback (rendering).

In some cases use of this permission may affect other
applications because the audio from one line may be mixed with other
audio being played on the system, or because manipulation of a mixer
affects the audio for all lines using that mixer.

record

Audio recording through the audio device or devices on the system.
Allows the application to obtain and manipulate lines and mixers for
audio recording (capture).

In some cases use of this permission may affect other applications
because manipulation of a mixer affects the audio for all lines using
that mixer. This permission can enable an applet or application to
eavesdrop on a user.

The following table lists the possible

AudioPermission

target names.
For each name, the table provides a description of exactly what that
permission allows, as well as a discussion of the risks of granting code the
permission.

Permission target name, what the permission allows, and associated
risks

Permission Target Name

What the Permission Allows

Risks of Allowing this Permission

play

Audio playback through the audio device or devices on the system.
Allows the application to obtain and manipulate lines and mixers for
audio playback (rendering).

In some cases use of this permission may affect other
applications because the audio from one line may be mixed with other
audio being played on the system, or because manipulation of a mixer
affects the audio for all lines using that mixer.

record

Audio recording through the audio device or devices on the system.
Allows the application to obtain and manipulate lines and mixers for
audio recording (capture).

In some cases use of this permission may affect other applications
because manipulation of a mixer affects the audio for all lines using
that mixer. This permission can enable an applet or application to
eavesdrop on a user.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AudioPermission

​(

String

name)

Creates a new

AudioPermission

object that has the specified
symbolic name, such as "play" or "record".

AudioPermission

​(

String

name,

String

actions)

Creates a new

AudioPermission

object that has the specified
symbolic name, such as "play" or "record".

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

AudioPermission

​(

String

name)

Creates a new

AudioPermission

object that has the specified
symbolic name, such as "play" or "record".

AudioPermission

​(

String

name,

String

actions)

Creates a new

AudioPermission

object that has the specified
symbolic name, such as "play" or "record".

---

#### Constructor Summary

Creates a new

AudioPermission

object that has the specified
symbolic name, such as "play" or "record".

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

- AudioPermission

```java
public AudioPermission​(
String
name)
```

Creates a new

AudioPermission

object that has the specified
symbolic name, such as "play" or "record". An asterisk can be used to
indicate all audio permissions.

**Parameters:** name

- the name of the new

AudioPermission
**Throws:** NullPointerException

- if

name

is

null
**Throws:** IllegalArgumentException

- if

name

is empty

- AudioPermission

```java
public AudioPermission​(
String
name,

String
actions)
```

Creates a new

AudioPermission

object that has the specified
symbolic name, such as "play" or "record". The

actions

parameter
is currently unused and should be

null

.

**Parameters:** name

- the name of the new

AudioPermission
**Parameters:** actions

- (unused; should be

null

)
**Throws:** NullPointerException

- if

name

is

null
**Throws:** IllegalArgumentException

- if

name

is empty

Constructor Detail

- AudioPermission

```java
public AudioPermission​(
String
name)
```

Creates a new

AudioPermission

object that has the specified
symbolic name, such as "play" or "record". An asterisk can be used to
indicate all audio permissions.

**Parameters:** name

- the name of the new

AudioPermission
**Throws:** NullPointerException

- if

name

is

null
**Throws:** IllegalArgumentException

- if

name

is empty

- AudioPermission

```java
public AudioPermission​(
String
name,

String
actions)
```

Creates a new

AudioPermission

object that has the specified
symbolic name, such as "play" or "record". The

actions

parameter
is currently unused and should be

null

.

**Parameters:** name

- the name of the new

AudioPermission
**Parameters:** actions

- (unused; should be

null

)
**Throws:** NullPointerException

- if

name

is

null
**Throws:** IllegalArgumentException

- if

name

is empty

---

#### Constructor Detail

AudioPermission

```java
public AudioPermission​(
String
name)
```

Creates a new

AudioPermission

object that has the specified
symbolic name, such as "play" or "record". An asterisk can be used to
indicate all audio permissions.

**Parameters:** name

- the name of the new

AudioPermission
**Throws:** NullPointerException

- if

name

is

null
**Throws:** IllegalArgumentException

- if

name

is empty

---

#### AudioPermission

public AudioPermission​(

String

name)

Creates a new

AudioPermission

object that has the specified
symbolic name, such as "play" or "record". An asterisk can be used to
indicate all audio permissions.

AudioPermission

```java
public AudioPermission​(
String
name,

String
actions)
```

Creates a new

AudioPermission

object that has the specified
symbolic name, such as "play" or "record". The

actions

parameter
is currently unused and should be

null

.

**Parameters:** name

- the name of the new

AudioPermission
**Parameters:** actions

- (unused; should be

null

)
**Throws:** NullPointerException

- if

name

is

null
**Throws:** IllegalArgumentException

- if

name

is empty

---

#### AudioPermission

public AudioPermission​(

String

name,

String

actions)

Creates a new

AudioPermission

object that has the specified
symbolic name, such as "play" or "record". The

actions

parameter
is currently unused and should be

null

.

---

