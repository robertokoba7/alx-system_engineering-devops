# Web stack debugging #3
---
The web stack I am debugging today is a Wordpress website running on a LAMP stack.

## Technologies
---
  `puppet-lint` version 2.1.1

## Files
---
 **Filename**                | **Description**
-----------------------------|-----------------
`0-strace_is_your_friend.pp` | Finds out why Apache is returning a 500 error by use of `strace`
