# You are given an initial list of events,
#  where each event has a unique eventId and a priority.
# Implement the EventManager class:
#  - EventManager(int[][] events) Initializes the manager with the given events,
#     where events[i] = [eventIdi, priority​​​​​​​i].
#  - void updatePriority(int eventId, int newPriority) Updates the priority
#     of the active event with id eventId to newPriority.
#  - int pollHighest() Removes and returns the eventId of the active event
#     with the highest priority. If multiple active events have the same priority,
#     return the smallest eventId among them. If there are no active events, return -1.
# An event is called active if it has not been removed by pollHighest().
# --- --- --- ---
# 1 <= events.length <= 10 ** 5
# events[i] = [eventId, priority]
# 1 <= eventId <= 10 ** 9
# 1 <= priority <= 10 ** 9
# All the values of eventId in events are unique.
# 1 <= newPriority <= 10 ** 9
# For every call to updatePriority, eventId refers to an active event.
# At most 10 ** 5 calls in total will be made to updatePriority and pollHighest.
import heapq


class EventManager:
    # working_solution: (12.91%, 8375%) -> (367ms, 85.19mb)  Time: O(n * log n) Space: O(n)

    def __init__(self, events: list[list[int]]) -> None:
        self.f_heap: list[tuple[int, int]] = []
        heapq.heapify(self.f_heap)
        for event, priority in events:
            heapq.heappush(
                self.f_heap, (-1 * priority, event)
            )
        self.f_events: dict[int, int] = {
            event: priority for event, priority in events
        }

    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.f_events[eventId] = newPriority
        heapq.heappush(
            self.f_heap, (-1 * newPriority, eventId)
        )

    def pollHighest(self) -> int:
        # Heap can have old data, recheck until we get the correct option.
        # ! 1 <= eventId <= 10 ** 9 !
        h_event: int = -1
        h_priority: int = -1
        while (
            self.f_events
            and
            self.f_heap
            and
            (h_event not in self.f_events or self.f_events[h_event] != h_priority)
        ):
            h_data: tuple[int, int] = heapq.heappop(self.f_heap)
            h_priority = -1 * h_data[0]
            h_event = h_data[1]
        # ! Removes and returns the eventId of the active event !
        if h_event in self.f_events:
            del self.f_events[h_event]

        return h_event
