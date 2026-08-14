# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explored object-oriented programming concepts in Python, including inheritance, class and instance namespaces, shallow copying, deep copying, and special methods.

## Implementation Summary

I implemented a server-management scenario to demonstrate the required concepts. The parent `Server` class was created with the class variable `device_type` and the instance variables `hostname` and `memory_gb`. Its constructor validated memory values and provided a default hostname when a hostname was missing. The class also included `display_info()` and `has_enough_memory()` methods.

I created a `CloudServer` child class that inherited from `Server`. It added the class variable `provider` and the instance variables `region`, `server_id`, and `services`. The child class reused the parent constructor with `super()`, added an `add_service()` method, and overrode `display_info()` to show cloud-specific information.

## Namespace Demonstration

I created two `CloudServer` objects and accessed the `provider` class variable through both the `CloudServer` class and an object. I added a `maintenance_window` attribute to only one object after construction and displayed both instance namespaces with `__dict__`. This showed that instance attributes could differ between objects even when the objects belonged to the same class.

I also displayed selected entries from the `CloudServer` class namespace to show that class variables and methods were stored at the class level instead of being duplicated inside every object.

## Shallow and Deep Copying

I used a `CloudServer` object whose `services` attribute contained a list of dictionaries with nested port lists. I created one copy with `copy()` and another with `deepcopy()`.

After modifying the original object's nested service data, the shallow copy reflected the same changes because it still referenced the same mutable `services` list. The deep copy did not change because its nested data had been copied independently. This demonstrated how shallow copying could save memory but also create unintended shared-state behavior, while deep copying used additional memory to provide independence.

## Edge Cases and Error Handling

I tested a missing hostname and allowed the constructor to replace it with `unnamed-server`. I also tested an empty service name. The `add_service()` method raised a `ValueError`, and the test code caught the exception so the program continued instead of terminating unexpectedly.

The program also demonstrated an initially empty `services` list, which showed that each `CloudServer` object received its own mutable list rather than sharing one list across instances.

## Student-Created Extension

I added the `__len__()` special method to `CloudServer`. This allowed `len(cloud_server)` to return the number of services installed on that specific server. This extension provided a simple Python-style interface while demonstrating how special methods could customize object behavior.

## Real-World Application

The class structure represented a simplified server-management system. A general server shared common information such as hostname and memory, while a cloud server extended that design with provider, region, server ID, and service information. A larger application could reuse the same parent class for additional server types while keeping common behavior in one place.

## How to Run

Run the program with Python 3:

```bash
python unit1_discussion.py
```

The program displayed the parent and child objects, inherited behavior, the student-created extension, edge-case handling, namespace behavior, and shallow/deep copy behavior.

## Reflection

During working on this assignment I learned how inheritance, namespaces, and object copying interact together in Python. I created a parent Server class and a CloudServer child class, then used super() to reuse the parent constructor while adding cloud-specific attributes and behaviors. Visualizing namespaces helped me understand that the storage of class variables and methods differs from that of individual object attributes. The section on object copying proved the most challenging; while a shallow copy might initially appear independent, nested mutable data can still be shared between the original and the copy. I addressed this issue by copying the list of services using both `copy()` and `deepcopy()` and then modifying the original data. Compared with procedural programming, OOP required more planning because responsibilities were organized into classes and objects instead of a sequence of functions. Although this entailed some additional upfront effort, it made the program easier to maintain, extend, and reuse. In practice, reusable classes can reduce code redundancy and make modifications more manageable. I could apply this same approach to future server management or cloud-based applications where multiple related objects share common behaviors yet require specific functionalities.
