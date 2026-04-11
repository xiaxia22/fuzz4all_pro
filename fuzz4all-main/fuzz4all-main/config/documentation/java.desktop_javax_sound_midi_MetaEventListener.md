# Interface MetaEventListener

**Source:** `java.desktop\javax\sound\midi\MetaEventListener.html`

### Class Description

```java
public interface
MetaEventListener

extends
EventListener
```

The

MetaEventListener

interface should be implemented by classes
whose instances need to be notified when a

Sequencer

has processed a

MetaMessage

. To register a

MetaEventListener

object to
receive such notifications, pass it as the argument to the

addMetaEventListener

method of

Sequencer

.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void meta​(
MetaMessage
meta)

Invoked when a

Sequencer

has encountered and processed a

MetaMessage

in the

Sequence

it is processing.

**Parameters:**
- meta

- the meta-message that the sequencer encountered

---

### Additional Sections

#### Interface MetaEventListener

**All Superinterfaces:** EventListener

```java
public interface
MetaEventListener

extends
EventListener
```

The

MetaEventListener

interface should be implemented by classes
whose instances need to be notified when a

Sequencer

has processed a

MetaMessage

. To register a

MetaEventListener

object to
receive such notifications, pass it as the argument to the

addMetaEventListener

method of

Sequencer

.

public interface

MetaEventListener

extends

EventListener

The

MetaEventListener

interface should be implemented by classes
whose instances need to be notified when a

Sequencer

has processed a

MetaMessage

. To register a

MetaEventListener

object to
receive such notifications, pass it as the argument to the

addMetaEventListener

method of

Sequencer

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

meta

​(

MetaMessage

meta)

Invoked when a

Sequencer

has encountered and processed a

MetaMessage

in the

Sequence

it is processing.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

meta

​(

MetaMessage

meta)

Invoked when a

Sequencer

has encountered and processed a

MetaMessage

in the

Sequence

it is processing.

---

#### Method Summary

Invoked when a

Sequencer

has encountered and processed a

MetaMessage

in the

Sequence

it is processing.

============ METHOD DETAIL ==========

- Method Detail

- meta

```java
void meta​(
MetaMessage
meta)
```

Invoked when a

Sequencer

has encountered and processed a

MetaMessage

in the

Sequence

it is processing.

**Parameters:** meta

- the meta-message that the sequencer encountered

Method Detail

- meta

```java
void meta​(
MetaMessage
meta)
```

Invoked when a

Sequencer

has encountered and processed a

MetaMessage

in the

Sequence

it is processing.

**Parameters:** meta

- the meta-message that the sequencer encountered

---

#### Method Detail

meta

```java
void meta​(
MetaMessage
meta)
```

Invoked when a

Sequencer

has encountered and processed a

MetaMessage

in the

Sequence

it is processing.

**Parameters:** meta

- the meta-message that the sequencer encountered

---

#### meta

void meta​(

MetaMessage

meta)

Invoked when a

Sequencer

has encountered and processed a

MetaMessage

in the

Sequence

it is processing.

---

