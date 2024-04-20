import pytest
import requests
#import logging
from Utilities.BaseClass import BaseClass
from testData.DataProvider import DataProvider


class TestRest(BaseClass, DataProvider):
    user_id = ""  # Class variable

    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self):
        self.base_class = BaseClass()

    @pytest.fixture(params=DataProvider.headers)
    def getHeaders(self, request):
        return request.param

    @pytest.fixture(params=DataProvider.requestPayload)
    def getReqPayload(self, request):
        return request.param

    @pytest.fixture(params=DataProvider.updatedPayload)
    def getUpdatedPayload(self, request):
        return request.param

    def test_createUser(self, getHeaders, getReqPayload):
        """Test user creation and profile information update."""
        url = f"{DataProvider.base_url}public/v2/users"
        response = requests.request('POST', url=url, headers=getHeaders, json=getReqPayload)

        # Verify user creation success
        assert response.status_code == 201, f"Failed to create user. Status code: {response.status_code}"
        user_data = response.json()
        assert user_data.get("id"), "User ID not received in response"
        TestRest.user_id = user_data["id"]
        self.logger.info("User ID after creation: %s", TestRest.user_id)

        # Verify profile information is updated correctly
        assert user_data.get("name") == getReqPayload.get("name"), "Name not updated correctly"
        assert user_data.get("email") == getReqPayload.get("email"), "Email not updated correctly"
        assert user_data.get("gender") == getReqPayload.get("gender"), "Gender not updated correctly"
        assert user_data.get("status") == getReqPayload.get("status"), "Status not updated correctly"

    def test_authenticateUser(self, getHeaders):
        """Test user authentication and profile information."""
        # Get user_id from TestUserOps
        user_id = TestRest.user_id
        self.logger.info("user_id: %s", user_id)
        url = f"{DataProvider.base_url}public/v2/users/{user_id}"
        response = requests.get(url=url, headers=getHeaders)

        # Implement error handling
        if response.status_code == 200:
            # Verify profile information is updated correctly
            user_data = response.json()
            assert user_data.get("id") == user_id, "User ID mismatch"
            assert user_data.get("name"), "Name not available"
            assert user_data.get("email"), "Email not available"
            assert user_data.get("gender"), "Gender not available"
            assert user_data.get("status"), "Status not available"
        elif response.status_code == 401:
            # Invalid user ID error handling
            assert False, "Invalid credentials"
        elif response.status_code == 403:
            # Invalid token error handling
            assert False, "Missing token"
        else:
            # Unexpected error handling
            assert False, f"Unexpected error. Status code: {response.status_code}"

        self.logger.info("Response: %s", response.json())

    def test_updateName(self, getHeaders, getUpdatedPayload):
        """Test updating user's name."""
        user_id = TestRest.user_id
        self.logger.info("user_id: %s", user_id)
        url = f"{DataProvider.base_url}public/v2/users/{user_id}"
        response = requests.put(url=url, headers=getHeaders, json=getUpdatedPayload)

        # Verify update success
        assert response.status_code == 200, f"Failed to update user. Status code: {response.status_code}"
        updated_user = response.json()
        self.logger.info("Updated user profile: %s", updated_user)
        assert updated_user.get("name") == getUpdatedPayload.get("name"), "Name not updated correctly"
        assert updated_user.get("email") == getUpdatedPayload.get("email"), "Email not updated correctly"
        self.logger.info("Profile updated successfully.")

    def test_cleanup_data(self, getHeaders):
        """Cleanup test data after execution."""
        user_id = TestRest.user_id
        self.logger.info("Cleanup data for user_id: %s", user_id)
        if user_id:
            # Delete user using the obtained user_id
            url = f"{DataProvider.base_url}public/v2/users/{user_id}"
            response = requests.delete(url=url, headers=getHeaders)
            assert response.status_code == 204, f"Failed to cleanup test data. Status code: {response.status_code}"
            self.logger.info("Test data cleanup successful. Deleted user with ID: %s", user_id)
        else:
            self.logger.warning("No user data to cleanup.")