# Interface KeyEventPostProcessor

**Source:** `java.desktop\java\awt\KeyEventPostProcessor.html`

### Class Description

```java
@FunctionalInterface

public interface
KeyEventPostProcessor
```

A KeyEventPostProcessor cooperates with the current KeyboardFocusManager
in the final resolution of all unconsumed KeyEvents. KeyEventPostProcessors
registered with the current KeyboardFocusManager will receive KeyEvents
after the KeyEvents have been dispatched to and handled by their targets.
KeyEvents that would have been otherwise discarded because no Component in
the application currently owns the focus will also be forwarded to
registered KeyEventPostProcessors. This will allow applications to implement
features that require global KeyEvent post-handling, such as menu shortcuts.

Note that the KeyboardFocusManager itself implements KeyEventPostProcessor.
By default, the current KeyboardFocusManager will be the final
KeyEventPostProcessor in the chain. The current KeyboardFocusManager cannot
be completely deregistered as a KeyEventPostProcessor. However, if a
KeyEventPostProcessor reports that no further post-processing of the
KeyEvent should take place, the AWT will consider the event fully handled
and will take no additional action with regard to the event. (While it is
possible for client code to register the current KeyboardFocusManager as
a KeyEventPostProcessor one or more times, this is usually unnecessary and
not recommended.)

**All Known Implementing Classes:** DefaultFocusManager

,

DefaultKeyboardFocusManager

,

FocusManager

,

KeyboardFocusManager

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean postProcessKeyEvent​(
KeyEvent
e)

This method is called by the current KeyboardFocusManager, requesting
that this KeyEventPostProcessor perform any necessary post-processing
which should be part of the KeyEvent's final resolution. At the time
this method is invoked, typically the KeyEvent has already been
dispatched to and handled by its target. However, if no Component in
the application currently owns the focus, then the KeyEvent has not
been dispatched to any Component. Typically, KeyEvent post-processing
will be used to implement features which require global KeyEvent
post-handling, such as menu shortcuts. Note that if a
KeyEventPostProcessor wishes to dispatch the KeyEvent, it must use

redispatchEvent

to prevent the AWT from recursively
requesting that this KeyEventPostProcessor perform post-processing
of the event again.

If an implementation of this method returns

false

, then the
KeyEvent is passed to the next KeyEventPostProcessor in the chain,
ending with the current KeyboardFocusManager. If an implementation
returns

true

, the KeyEvent is assumed to have been fully
handled (although this need not be the case), and the AWT will take no
further action with regard to the KeyEvent. If an implementation
consumes the KeyEvent but returns

false

, the consumed
event will still be passed to the next KeyEventPostProcessor in the
chain. It is important for developers to check whether the KeyEvent has
been consumed before performing any post-processing of the KeyEvent. By
default, the current KeyboardFocusManager will perform no post-
processing in response to a consumed KeyEvent.

**Parameters:**
- e

- the KeyEvent to post-process

**Returns:**
- true

if the AWT should take no further action with
regard to the KeyEvent;

false

otherwise

**See Also:**
- KeyboardFocusManager.redispatchEvent(java.awt.Component, java.awt.AWTEvent)

---

### Additional Sections

#### Interface KeyEventPostProcessor

**All Known Implementing Classes:** DefaultFocusManager

,

DefaultKeyboardFocusManager

,

FocusManager

,

KeyboardFocusManager

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
KeyEventPostProcessor
```

A KeyEventPostProcessor cooperates with the current KeyboardFocusManager
in the final resolution of all unconsumed KeyEvents. KeyEventPostProcessors
registered with the current KeyboardFocusManager will receive KeyEvents
after the KeyEvents have been dispatched to and handled by their targets.
KeyEvents that would have been otherwise discarded because no Component in
the application currently owns the focus will also be forwarded to
registered KeyEventPostProcessors. This will allow applications to implement
features that require global KeyEvent post-handling, such as menu shortcuts.

Note that the KeyboardFocusManager itself implements KeyEventPostProcessor.
By default, the current KeyboardFocusManager will be the final
KeyEventPostProcessor in the chain. The current KeyboardFocusManager cannot
be completely deregistered as a KeyEventPostProcessor. However, if a
KeyEventPostProcessor reports that no further post-processing of the
KeyEvent should take place, the AWT will consider the event fully handled
and will take no additional action with regard to the event. (While it is
possible for client code to register the current KeyboardFocusManager as
a KeyEventPostProcessor one or more times, this is usually unnecessary and
not recommended.)

**Since:** 1.4
**See Also:** KeyboardFocusManager.addKeyEventPostProcessor(java.awt.KeyEventPostProcessor)

,

KeyboardFocusManager.removeKeyEventPostProcessor(java.awt.KeyEventPostProcessor)

@FunctionalInterface

public interface

KeyEventPostProcessor

A KeyEventPostProcessor cooperates with the current KeyboardFocusManager
in the final resolution of all unconsumed KeyEvents. KeyEventPostProcessors
registered with the current KeyboardFocusManager will receive KeyEvents
after the KeyEvents have been dispatched to and handled by their targets.
KeyEvents that would have been otherwise discarded because no Component in
the application currently owns the focus will also be forwarded to
registered KeyEventPostProcessors. This will allow applications to implement
features that require global KeyEvent post-handling, such as menu shortcuts.

Note that the KeyboardFocusManager itself implements KeyEventPostProcessor.
By default, the current KeyboardFocusManager will be the final
KeyEventPostProcessor in the chain. The current KeyboardFocusManager cannot
be completely deregistered as a KeyEventPostProcessor. However, if a
KeyEventPostProcessor reports that no further post-processing of the
KeyEvent should take place, the AWT will consider the event fully handled
and will take no additional action with regard to the event. (While it is
possible for client code to register the current KeyboardFocusManager as
a KeyEventPostProcessor one or more times, this is usually unnecessary and
not recommended.)

Note that the KeyboardFocusManager itself implements KeyEventPostProcessor.
By default, the current KeyboardFocusManager will be the final
KeyEventPostProcessor in the chain. The current KeyboardFocusManager cannot
be completely deregistered as a KeyEventPostProcessor. However, if a
KeyEventPostProcessor reports that no further post-processing of the
KeyEvent should take place, the AWT will consider the event fully handled
and will take no additional action with regard to the event. (While it is
possible for client code to register the current KeyboardFocusManager as
a KeyEventPostProcessor one or more times, this is usually unnecessary and
not recommended.)

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

postProcessKeyEvent

​(

KeyEvent

e)

This method is called by the current KeyboardFocusManager, requesting
that this KeyEventPostProcessor perform any necessary post-processing
which should be part of the KeyEvent's final resolution.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

postProcessKeyEvent

​(

KeyEvent

e)

This method is called by the current KeyboardFocusManager, requesting
that this KeyEventPostProcessor perform any necessary post-processing
which should be part of the KeyEvent's final resolution.

---

#### Method Summary

This method is called by the current KeyboardFocusManager, requesting
that this KeyEventPostProcessor perform any necessary post-processing
which should be part of the KeyEvent's final resolution.

============ METHOD DETAIL ==========

- Method Detail

- postProcessKeyEvent

```java
boolean postProcessKeyEvent​(
KeyEvent
e)
```

This method is called by the current KeyboardFocusManager, requesting
that this KeyEventPostProcessor perform any necessary post-processing
which should be part of the KeyEvent's final resolution. At the time
this method is invoked, typically the KeyEvent has already been
dispatched to and handled by its target. However, if no Component in
the application currently owns the focus, then the KeyEvent has not
been dispatched to any Component. Typically, KeyEvent post-processing
will be used to implement features which require global KeyEvent
post-handling, such as menu shortcuts. Note that if a
KeyEventPostProcessor wishes to dispatch the KeyEvent, it must use

redispatchEvent

to prevent the AWT from recursively
requesting that this KeyEventPostProcessor perform post-processing
of the event again.

If an implementation of this method returns

false

, then the
KeyEvent is passed to the next KeyEventPostProcessor in the chain,
ending with the current KeyboardFocusManager. If an implementation
returns

true

, the KeyEvent is assumed to have been fully
handled (although this need not be the case), and the AWT will take no
further action with regard to the KeyEvent. If an implementation
consumes the KeyEvent but returns

false

, the consumed
event will still be passed to the next KeyEventPostProcessor in the
chain. It is important for developers to check whether the KeyEvent has
been consumed before performing any post-processing of the KeyEvent. By
default, the current KeyboardFocusManager will perform no post-
processing in response to a consumed KeyEvent.

**Parameters:** e

- the KeyEvent to post-process
**Returns:** true

if the AWT should take no further action with
regard to the KeyEvent;

false

otherwise
**See Also:** KeyboardFocusManager.redispatchEvent(java.awt.Component, java.awt.AWTEvent)

Method Detail

- postProcessKeyEvent

```java
boolean postProcessKeyEvent​(
KeyEvent
e)
```

This method is called by the current KeyboardFocusManager, requesting
that this KeyEventPostProcessor perform any necessary post-processing
which should be part of the KeyEvent's final resolution. At the time
this method is invoked, typically the KeyEvent has already been
dispatched to and handled by its target. However, if no Component in
the application currently owns the focus, then the KeyEvent has not
been dispatched to any Component. Typically, KeyEvent post-processing
will be used to implement features which require global KeyEvent
post-handling, such as menu shortcuts. Note that if a
KeyEventPostProcessor wishes to dispatch the KeyEvent, it must use

redispatchEvent

to prevent the AWT from recursively
requesting that this KeyEventPostProcessor perform post-processing
of the event again.

If an implementation of this method returns

false

, then the
KeyEvent is passed to the next KeyEventPostProcessor in the chain,
ending with the current KeyboardFocusManager. If an implementation
returns

true

, the KeyEvent is assumed to have been fully
handled (although this need not be the case), and the AWT will take no
further action with regard to the KeyEvent. If an implementation
consumes the KeyEvent but returns

false

, the consumed
event will still be passed to the next KeyEventPostProcessor in the
chain. It is important for developers to check whether the KeyEvent has
been consumed before performing any post-processing of the KeyEvent. By
default, the current KeyboardFocusManager will perform no post-
processing in response to a consumed KeyEvent.

**Parameters:** e

- the KeyEvent to post-process
**Returns:** true

if the AWT should take no further action with
regard to the KeyEvent;

false

otherwise
**See Also:** KeyboardFocusManager.redispatchEvent(java.awt.Component, java.awt.AWTEvent)

---

#### Method Detail

postProcessKeyEvent

```java
boolean postProcessKeyEvent​(
KeyEvent
e)
```

This method is called by the current KeyboardFocusManager, requesting
that this KeyEventPostProcessor perform any necessary post-processing
which should be part of the KeyEvent's final resolution. At the time
this method is invoked, typically the KeyEvent has already been
dispatched to and handled by its target. However, if no Component in
the application currently owns the focus, then the KeyEvent has not
been dispatched to any Component. Typically, KeyEvent post-processing
will be used to implement features which require global KeyEvent
post-handling, such as menu shortcuts. Note that if a
KeyEventPostProcessor wishes to dispatch the KeyEvent, it must use

redispatchEvent

to prevent the AWT from recursively
requesting that this KeyEventPostProcessor perform post-processing
of the event again.

If an implementation of this method returns

false

, then the
KeyEvent is passed to the next KeyEventPostProcessor in the chain,
ending with the current KeyboardFocusManager. If an implementation
returns

true

, the KeyEvent is assumed to have been fully
handled (although this need not be the case), and the AWT will take no
further action with regard to the KeyEvent. If an implementation
consumes the KeyEvent but returns

false

, the consumed
event will still be passed to the next KeyEventPostProcessor in the
chain. It is important for developers to check whether the KeyEvent has
been consumed before performing any post-processing of the KeyEvent. By
default, the current KeyboardFocusManager will perform no post-
processing in response to a consumed KeyEvent.

**Parameters:** e

- the KeyEvent to post-process
**Returns:** true

if the AWT should take no further action with
regard to the KeyEvent;

false

otherwise
**See Also:** KeyboardFocusManager.redispatchEvent(java.awt.Component, java.awt.AWTEvent)

---

#### postProcessKeyEvent

boolean postProcessKeyEvent​(

KeyEvent

e)

This method is called by the current KeyboardFocusManager, requesting
that this KeyEventPostProcessor perform any necessary post-processing
which should be part of the KeyEvent's final resolution. At the time
this method is invoked, typically the KeyEvent has already been
dispatched to and handled by its target. However, if no Component in
the application currently owns the focus, then the KeyEvent has not
been dispatched to any Component. Typically, KeyEvent post-processing
will be used to implement features which require global KeyEvent
post-handling, such as menu shortcuts. Note that if a
KeyEventPostProcessor wishes to dispatch the KeyEvent, it must use

redispatchEvent

to prevent the AWT from recursively
requesting that this KeyEventPostProcessor perform post-processing
of the event again.

If an implementation of this method returns

false

, then the
KeyEvent is passed to the next KeyEventPostProcessor in the chain,
ending with the current KeyboardFocusManager. If an implementation
returns

true

, the KeyEvent is assumed to have been fully
handled (although this need not be the case), and the AWT will take no
further action with regard to the KeyEvent. If an implementation
consumes the KeyEvent but returns

false

, the consumed
event will still be passed to the next KeyEventPostProcessor in the
chain. It is important for developers to check whether the KeyEvent has
been consumed before performing any post-processing of the KeyEvent. By
default, the current KeyboardFocusManager will perform no post-
processing in response to a consumed KeyEvent.

If an implementation of this method returns

false

, then the
KeyEvent is passed to the next KeyEventPostProcessor in the chain,
ending with the current KeyboardFocusManager. If an implementation
returns

true

, the KeyEvent is assumed to have been fully
handled (although this need not be the case), and the AWT will take no
further action with regard to the KeyEvent. If an implementation
consumes the KeyEvent but returns

false

, the consumed
event will still be passed to the next KeyEventPostProcessor in the
chain. It is important for developers to check whether the KeyEvent has
been consumed before performing any post-processing of the KeyEvent. By
default, the current KeyboardFocusManager will perform no post-
processing in response to a consumed KeyEvent.

---

